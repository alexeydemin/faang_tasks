class Solution:
    def validIPAddress(self, ip: str) -> str:
        parts = ip.split('.')
        if len(parts) == 4:
            if all(len(x) and not (x[0] == '0' and len(x) > 1) and x.isdigit() and 0 <= int(x) < 256 for x in parts):
                return 'IPv4'
        parts = ip.split(':')
        if len(parts) == 8:
            if all(
                    0 < len(x) <= 4 and self.is_hex(x) for x in parts
            ):
                return 'IPv6'

        return 'Neither'

    def is_hex(self, s):
        import string
        return all(c in string.hexdigits for c in s)


# print(Solution().validIPAddress("255.0.0x.255"))  # Neither
# print(Solution().is_hex(''))
# print(Solution().validIPAddress("172.16.254.1")) #IPv4
print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))  # IPv6
# print(Solution().validIPAddress("256.256.256.256")) #Neither#
