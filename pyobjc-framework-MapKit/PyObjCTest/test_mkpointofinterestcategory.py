import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKPointOfInterestCategory(TestCase):
        @min_os_level("10.15")
        def test_constants(self):
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryAirport, unicode)
            self.assertIsInstance(
                MapKit.MKPointOfInterestCategoryAmusementPark, unicode
            )
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryAquarium, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryATM, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryBakery, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryBank, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryBeach, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryBrewery, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryCafe, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryCampground, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryCarRental, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryEVCharger, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryFireStation, unicode)
            self.assertIsInstance(
                MapKit.MKPointOfInterestCategoryFitnessCenter, unicode
            )
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryFoodMarket, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryGasStation, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryHospital, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryHotel, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryLaundry, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryLibrary, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryMarina, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryMovieTheater, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryMuseum, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryNationalPark, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryNightlife, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryPark, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryParking, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryPharmacy, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryPolice, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryPostOffice, unicode)
            self.assertIsInstance(
                MapKit.MKPointOfInterestCategoryPublicTransport, unicode
            )
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryRestaurant, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryRestroom, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategorySchool, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryStadium, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryStore, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryTheater, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryUniversity, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryWinery, unicode)
            self.assertIsInstance(MapKit.MKPointOfInterestCategoryZoo, unicode)


if __name__ == "__main__":
    main()
