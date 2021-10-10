from PyObjCTools
        .TestSupport import*

            import Security

    class Testemmspi(TestCase)
    :

      def test_unsuppported(self)
    : self.assertFalse(hasattr(Security, 'CSSM_STATE_FUNCS')) self
        .assertFalse(hasattr(Security, 'CSSM_MANAGER_REGISTRATION_INFO')) self
        .assertFalse(hasattr(Security, 'CSSM_HINT_NONE')) self
        .assertFalse(hasattr(Security, 'CSSM_HINT_ADDRESS_APP')) self
        .assertFalse(hasattr(Security, 'CSSM_HINT_ADDRESS_SP')) self.assertFalse(
            hasattr(Security, 'ModuleManagerAuthenticate'))

            if __name__
    == "__main__" : main()
