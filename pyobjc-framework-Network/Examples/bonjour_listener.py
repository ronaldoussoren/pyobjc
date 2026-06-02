"""
Start a bonjour braowser and print the results
from one batch of updates for the "_http._tcp"
group (e.g. local webservers registered with bonjour)
"""

import Network
import dispatch
import os

descriptor = Network.nw_browse_descriptor_create_bonjour_service(b"_http._tcp", None)
parameters = None
browser = Network.nw_browser_create(descriptor, parameters)


def results_handler(old_result, new_result, batch_complete):
    print(f"{old_result=}")
    print(f"{new_result=}")
    print(f"{batch_complete=}")

    if batch_complete:
        os._exit(0)


Network.nw_browser_set_queue(browser, dispatch.dispatch_get_main_queue())
Network.nw_browser_set_browse_results_changed_handler(browser, results_handler)
Network.nw_browser_start(browser)

dispatch.dispatch_main()
