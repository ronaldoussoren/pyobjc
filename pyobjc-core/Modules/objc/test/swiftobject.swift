import Foundation

class PyObjCTestObject {
    @objc(init)
    func initValue() -> Any {
        return self;
    }

    @objc
    func value() -> Int {
       return 42;
    }
}
