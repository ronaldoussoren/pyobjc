function FindProxyForURL(url, host) {
   if (shExpMatch(host, "*.apple.com")) {
         return "PROXY proxy.apple.com:8080";
    }
    return "DIRECT";
}

