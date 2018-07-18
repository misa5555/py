class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        import re
        pt = 0
        path_list = []
        while pt < len(path):
            drc = re.match(r'\/[^\/]*', path[pt:]).group()
            if drc == "/..":
                if path_list:
                    path_list.pop()
            elif drc != '/.':
                path_list.append(drc)

            pt += len(drc)

        full_path = ''.join(path_list)
        if full_path and full_path[-1] == '/':
            full_path = full_path[:-1]
        if not full_path:
            full_path = "/"
        print(full_path)
        return full_path

s = Solution()
s.simplifyPath("/home/")
s.simplifyPath("/a/./b/../../c/")
s.simplifyPath('/.')