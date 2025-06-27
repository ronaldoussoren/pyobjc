// objective.metadata exceptions file, see its document
// for information on how to update this file.
{
 "definitions": {
  "typed_enum": {
   "FSTaskParameterConstant":  { "type": "@", "type_name": "NSString" }
  },
  "externs": {
   "FSKitVersionString": { "ignore": true }
  },
  "classes": {
   "NSObject": {
    "methods": [
     {
      "selector": "preallocate:offset:length:flags:usingPacker:replyHandler:",
      "class_method": false,
      "args": {
       "4": {
        "callable": {
         "arguments": {
          "0": { "type": "^v" },
          "1": { "type": "@" },
          "2": { "type": "i" },
          "3": { "type": "Q" },
          "4": { "type": "Q" },
          "5": { "type": "I" }
         },
         "retval": { "type": "i" }
        }
       }
      }
     },
     {
      "selector": "lookupName:inDirectory:usingPacker:replyHandler:",
      "class_method": false,
      "args": {
       "2": {
        "callable": {
         "arguments": {
          "0": { "type": "^v" },
          "1": { "type": "@" },
          "2": { "type": "i" },
          "3": { "type": "Q" },
          "4": { "type": "Q" },
          "5": { "type": "I" }
         },
         "retval": { "type": "i" }
        }
       }
      }
     },
     {
      "selector": "blockmapFile:range:startIO:flags:operationID:usingPacker:replyHandler:",
      "class_method": false,
      "args": {
       "5": {
        "callable": {
         "arguments": {
          "0": { "type": "^v" },
          "1": { "type": "@" },
          "2": { "type": "i" },
          "3": { "type": "Q" },
          "4": { "type": "Q" },
          "5": { "type": "I" }
         },
         "retval": { "type": "Z" }
        }
       }
      }
     },
     {
      "selector": "createItemNamed:type:inDirectory:attributes:usingPacker:replyHandler:",
      "class_method": false,
      "args": {
       "4": {
        "callable": {
         "arguments": {
          "0": { "type": "^v" },
          "1": { "type": "@" },
          "2": { "type": "i" },
          "3": { "type": "Q" },
          "4": { "type": "Q" },
          "5": { "type": "I" }
         },
         "retval": { "type": "i" }
        }
       }
      }
     },
     {
      "selector": "enumerateDirectory:startingAtCookie:verifier:provideAttributes:attributes:usingBlock:replyHandler:",
      "class_method": false,
      "args": {
       "5": {
        "callable": {
         "arguments": {
          "0": { "type": "^v" },
          "1": { "type": "@" },
          "2": { "type": "C" },
          "3": { "type": "Q" },
          "4": { "type": "Q" },
          "5": { "type": "@" },
          "6": { "type": "B" }
         },
         "retval": { "type": "i" }
        }
       }
      }
     }
    ]
   },
   "FSBlockDeviceResource": {
    "methods": [
     {
      "args": {
       "0": { "type_modifier": "o", "c_array_length_in_arg": 2 },
       "3": { "type_modifier": "o" }
      },
      "class_method": false,
      "selector": "readInto:startingAt:length:error:"
     },
     {
      "args": {
       "0": { "type_modifier": "N", "c_array_length_in_arg": 2 }
      },
      "class_method": false,
      "selector": "readInto:startingAt:length:completionHandler:"
     },
     {
      "args": {
       "0": { "type_modifier": "N", "c_array_length_in_arg": 2 }
      },
      "class_method": false,
      "selector": "readInto:startingAt:length:replyHandler:"
     },
     {
      "args": {
       "0": { "type_modifier": "N", "c_array_length_in_arg": 2 }
      },
      "class_method": false,
      "selector": "synchronousReadInto:startingAt:length:replyHandler:"
     },
     {
      "args": {
       "0": { "type_modifier": "n", "c_array_length_in_arg": 2 },
       "3": { "type_modifier": "o" }
      },
      "class_method": false,
      "selector": "writeFrom:startingAt:length:error:"
     },
     {
      "args": {
       "0": { "type_modifier": "n", "c_array_length_in_arg": 2 }
      },
      "class_method": false,
      "selector": "writeFrom:startingAt:length:completionHandler:"
     },
     {
      "args": {
       "0": { "type_modifier": "n", "c_array_length_in_arg": 2 }
      },
      "class_method": false,
      "selector": "writeFrom:startingAt:length:replyHandler:"
     },
     {
      "selector": "metadataReadInto:startingAt:length:",
      "class_method": false,
      "args": {
       "0": { "type_modifier": "o", "c_array_length_in_arg": 2 }
      }
     },
     {
      "args": {
       "0": { "type_modifier": "o", "c_array_length_in_arg": 2},
       "3": { "type_modifier": "n", "c_array_length_in_arg": 4 }
      },
      "class_method": false,
      "selector": "metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:"
     },
     {
      "args": {
       "0": { "type_modifier": "n", "c_array_length_in_arg": 2 }
      },
      "class_method": false,
      "selector": "metadataWriteFrom:startingAt:length:"
     },
     {
      "args": {
       "0": { "type_modifier": "n", "c_array_length_in_arg": 2 }
      },
      "class_method": false,
      "selector": "delayedMetadataWriteFrom:startingAt:length:"
     }
    ]
   },
   "FSEntityIdentifier": {
    "methods": [
     {
      "args": {
       "1": { "type_override": "^v", "type_modifier": "n", "c_array_of_variable_length": true }
      },
      "class_method": false,
      "selector": "initWithUUID:byteQualifier:"
     },
     {
      "args": {
       "1": { "type_override": "^v", "type_modifier": "n", "c_array_of_variable_length": true }
      },
      "class_method": false,
      "selector": "initWithUUID:longByteQualifier:"
     },
     {
      "args": {
       "1": { "type_override": "^v", "type_modifier": "n", "c_array_of_variable_length": true }
      },
      "class_method": true,
      "selector": "identifierWithUUID:byteQualifier:"
     },
     {
      "args": {
       "1": { "type_override": "^v", "type_modifier": "n", "c_array_of_variable_length": true }
      },
      "class_method": true,
      "selector": "identifierWithUUID:longByteQualifier:"
     }
    ]
   },
   "FSFileDataBuffer": {
    "methods": [
     {
      "class_method": false,
      "retval": { "c_array_of_variable_length": true },
      "selector": "bytes"
     },
     {
      "class_method": false,
      "args": {
       "0": {
        "callable": {
         "arguments": {
          "0": { "type": "^v" },
          "1": { "c_array_of_variable_length": true, "type_modifier": "n", "type": "^v"  }
         },
         "retval": { "type": "v" }
        }
       }
      },
      "selector": "withBytes:"
     }
    ]
   },
   "FSFileName": {
    "methods": [
     {
      "args": {
       "0": { "type_modifier": "n", "c_array_delimited_by_null": true }
      },
      "class_method": false,
      "selector": "initWithCString:"
     },
     {
      "args": {
       "0": { "type_override": "^v", "type_modifier": "n", "c_array_length_in_arg": 1 }
      },
      "class_method": false,
      "selector": "initWithBytes:length:"
     },
     {
      "args": {
       "0": { "type_modifier": "n", "c_array_delimited_by_null": true }
      },
      "class_method": true,
      "selector": "nameWithCString:"
     },
     {
      "args": {
       "0": { "type_override": "^v", "type_modifier": "n", "c_array_length_in_arg": 1 }
      },
      "class_method": true,
      "selector": "nameWithBytes:length:"
     }
    ]
   },
   "FSItemAttributes": {
    "methods": [
     {
      "args": {
       "0": { "type_modifier": "o" }
      },
      "class_method": false,
      "selector": "modifyTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "o" }
      },
      "class_method": false,
      "selector": "addedTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "o" }
      },
      "class_method": false,
      "selector": "changeTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "o" }
      },
      "class_method": false,
      "selector": "accessTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "o" }
      },
      "class_method": false,
      "selector": "birthTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "o" }
      },
      "class_method": false,
      "selector": "backupTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "n" }
      },
      "class_method": false,
      "selector": "setModifyTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "n" }
      },
      "class_method": false,
      "selector": "setAddedTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "n" }
      },
      "class_method": false,
      "selector": "setChangeTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "n" }
      },
      "class_method": false,
      "selector": "setAccessTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "n" }
      },
      "class_method": false,
      "selector": "setBirthTime:"
     },
     {
      "args": {
       "0": { "type_modifier": "n" }
      },
      "class_method": false,
      "selector": "setBackupTime:"
     }
    ]
   },
   "FSMessageConnection": {
    "methods": [
     {
      "class_method": false,
      "selector": "logLocalizedMessage:table:bundle:",
      "variadic": true,
      "args": {
       "0": { "printf_format": true }
      }
     },
     {
      "class_method": false,
      "selector": "localizedMessage:table:bundle:",
      "variadic": true,
      "args": {
       "0": { "printf_format": true }
      }
     },
     {
      "args": {
       "3": {}
      },
      "class_method": false,
      "selector": "logLocalizedMessage:table:bundle:arguments:",
      "suggestion": "Use one of the other log methods"
     }
    ]
   },
   "FSMutableFileDataBuffer": {
    "methods": [
     {
      "class_method": false,
      "retval": { "c_array_of_variable_length": true },
      "selector": "mutableBytes"
     },
     {
      "class_method": false,
      "args": {
       "0": {
        "callable": {
         "arguments": {
          "0": { "type": "^v" },
          "1": { "c_array_of_variable_length": true, "type_modifier": "N", "type": "^v"  }
         },
         "retval": { "type": "v" }
        }
       }
      },
      "selector": "withMutableBytes:"
     }
    ]
   },
   "FSTaskOptionsBundle": {
    "methods": [
     {
      "args": {
       "0": {}
      },
      "class_method": true,
      "selector": "bundleForArguments:count:extension:operationType:errorHandler:"
     }
    ]
   }
  },
  "formal_protocols": {},
  "functions": {},
  "informal_protocols": {}
 }
}
