import sys


class MostFrequentIpAddress:
    """
    Problem statement: Given a list of logs with IP addresses in the following format.
    lines = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
    "10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
    "10.0.0.2 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
    "10.0.0.2 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
    "10.0.0.3 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]

    Return the most frequent IP address from the logs. The retuned IP address value must be in
    a string format. If multiple IP addresses have the count equal to max count, then return
    the address as a comma-separated string with IP addresses in sorted order.

    Logic: Split the log sentences at the end of Ip address and use that as our input
    Then maintain a dictionary having ip address and its value just like a map
    Figure out the maximum count, and then take a list of IPs from dictionary who have their count
    equal to maximum count
    """
    def mostFrequentIpAddress(self, lines: list[str]) -> str:
        ans = {}
        maxIp = -sys.maxsize
        for line in lines:
            s = line[:8]
            ans[s] = ans.get(s,0) + 1
            maxIp = max(maxIp,ans[s])

        maxIps = [Ip for Ip,Count in ans.items() if ans[Ip]==maxIp]
        #print(maxIps)
        if len(maxIps)>1:
            return ",".join(sorted(maxIps))
        else:
            return maxIps[0]


    def main(self):
        lines = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
                 "10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
                 "10.0.0.2 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
                 "10.0.0.2 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
                 "10.0.0.3 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]

        print(self.mostFrequentIpAddress(lines))

most = MostFrequentIpAddress()
most.main()