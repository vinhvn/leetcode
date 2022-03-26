class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = defaultdict(int)
        
        # build hashmap of cpdomains
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            subdomains = domain.split(".")
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                hashmap[subdomain] += int(count)
        
        # build output cpdomains
        output = []
        for subdomain, count in hashmap.items():
            output.append(f"{str(count)} {subdomain}")
        return output
