import Accounts
import Cocoa

st = Accounts.ACAccountStore.alloc().init()

def cb(granted, error):
    if granted:
        print(st.accounts())
        print(st.accountsWithAccountType_(tp))

    else:
        print("Not allowed")
        print(error)

    global running
    running = False

tp = st.accountTypeWithAccountTypeIdentifier_(Accounts.ACAccountTypeIdentifierTwitter)
print(tp)

st.requestAccessToAccountsWithType_options_completion_(tp, None, cb)

rl = Cocoa.NSRunLoop.currentRunLoop()

running = True
while running and rl.runMode_beforeDate_(Cocoa.NSDefaultRunLoopMode, Cocoa.NSDate.dateWithTimeIntervalSinceNow_(1.0)):
    pass

print("Done")
