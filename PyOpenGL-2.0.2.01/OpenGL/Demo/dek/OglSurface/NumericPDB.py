# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

import sys
import os
import string
import Numeric
import Geometry
import copy

GUAAtoms = [ "N2", "O6", "C6", "C5", "N7", "C8", "N9", "C4", "N3", "C2", "N1" ]

def rotmat(phi, theta, psi, tx=0, ty=0, tz=0):

	s1 = Numeric.sin(phi)
	s2 = Numeric.sin(theta)
	s3 = Numeric.sin(psi)
	c1 = Numeric.cos(phi)
	c2 = Numeric.cos(theta)
	c3 = Numeric.cos(psi)

	newmat = Numeric.array([
		[ c2*c3, s2*s1*c3 - c1*s3, s2*c1*c3 + s1*s3, 0],
		[ c2*s3, s2*s1*s3 + c1*c3, s2*c1*s3 - s1*c3, 0],
		[-s2, c2*s1, c2*c1, 0],
		[tx, ty, tz, 1]])

	return newmat

def matrix_apply(crd, mat):
	o = [crd[0], crd[1], crd[2], 1.0]
	n = [0.0, 0.0, 0.0, 0.0]

	for i in range(4):
		for j in range(4):
			n[i] = n[i] + o[j] * mat[j][i]
			
	new = [None, None, None]
	
	for i in range(3):
		new[i] = (n[i]/n[3])
	return new



class PDBRecord:
	def __init__(self, type=None, anum=None, atom=None, residue=None, chain=None, rnum=None):
		self.type = type
		self.anum = anum
		self.atom = atom
		self.residue = residue
		self.chain = chain
		self.rnum = rnum



class PDB:
	def __init__(self, filename = None, crds = None, records = None, connect = None):
		if crds == None:
			crds = []
		if records == None:
			records = []
		self.records = records
		self.crds = crds
		self.connect = connect

		if filename != None:
			sys.stderr.write("Reading in new PDB %s\n" % filename)
			self.Read(filename)


## note: we read the anum here, which doesn't necessarily correspond to the actual
## record number.
	def Read(self, filename):
		pdbfile = open(filename)
		sys.stderr.write("Opened '%s' for reading as PDB\n" % filename)

		while(1):
			line = pdbfile.readline()

			if line == '':
				break

			if line[0:4] == 'ATOM' or line[0:6] == 'HETATM':
				type = string.strip(line[0:6])
				anum = string.atoi(string.strip(line[7:11]))
				atom = string.strip(line[12:17])
				residue = string.strip(line[17:20])
				chain = string.strip(line[21:22])
				rnum = string.atoi(string.strip(line[23:26]))
				x = string.atof(string.strip(line[31:38]))
				y = string.atof(string.strip(line[39:46]))
				z = string.atof(string.strip(line[47:54]))

				self.records.append(PDBRecord(type, anum, atom, residue, chain, rnum))
				self.crds.append((x,y,z))
				
		
		self.crds = Numeric.array(self.crds)

	def Write(self, filename):
		self.pdbfd=open(filename,"w")
			
		for i in range(len(self.records)):
			record = self.records[i]
			self.pdbfd.write("%-6s%5d %-4s%c%-4s%c%4d%c   %8.3f%8.3f%8.3f\n" % \
							 ( record.type, record.anum, record.atom,' ', record.residue,' ', record.rnum, ' ', 
							   self.crds[i][0], self.crds[i][1], self.crds[i][2]))

		self.pdbfd.write("TER\n")

		if self.connect != None:
			for i in self.connect:
				self.pdbfd.write("CONECT")
				for j in i:
					self.pdbfd.write("%5d" % (j+1))
				self.pdbfd.write("\n")

		self.pdbfd.write("END\n")
		self.pdbfd.close()


	def Rotate(self,alpha, beta, gamma, tx, ty, tz):
		r = rotmat(alpha, beta, gamma, tx, ty, tz)
		self.RotateMatrix(r)

	def RotateMatrix(self,r):
		for i in range(len(self.crds)):
			self.crds[i] = matrix_apply(self.crds[i], r)

	def Center(self):
		center = Numeric.add.reduce(self.crds) / len(self.crds)
		self.crds = Numeric.subtract(self.crds, center)

	def Print(self):
		for i in self.records:
			print i.type, i.anum, i.atom, i.residue, i.chain, i.rnum

	def ReturnAnum(self, atom, rnum):
		for i in range(len(self.records)):
			record = self.records[i]
			if record.atom == atom and record.rnum == rnum:
 				return i
		sys.stderr.write("Unable to find atom '%s' in residue %d\n" % (atom, rnum))
		return None

	def CrdByName(self, atom, res):
		x = self.ReturnAnum(atom, res)
		if x == None:
			return None
		return self.crds[x]

	def FixResNum(self):
		rnum = 1
		for i in range(len(self.records)):
			newrnum = rnum
			if i < len(self.records)-1 and \
			   self.records[i+1].rnum != self.records[i].rnum:
				rnum = rnum + 1
			self.records[i].rnum = newrnum
			self.records[i].anum = i

	def Copy(self):
		crds = Numeric.array(self.crds)
		records = copy.copy(self.records)
		return PDB(None, crds, records)


	def Append(self, struct2):
		records = self.records + copy.copy(struct2.records)
		crds = Numeric.concatenate((self.crds, struct2.crds))

		return PDB(None, crds, records)

