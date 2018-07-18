class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str ex) "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        :rtype: int
        """
        import re
        from collections import defaultdict
        current_dirs = defaultdict(str)
        current_dirs[0] = "dir"
        i = 0
        ans = 0
        while i < len(input):
            matcher = re.match(r'\n*(\t*)([^\n]*)', input[i:])
            if matcher:
                i += len(matcher.group())
                level = len(matcher.group(1))
                dir_or_file = matcher.group(2)
                current_dirs[level] = dir_or_file
                if '.' in dir_or_file:
                    current_dirs = {k:v for (k,v) in current_dirs.items() if k <= level }
                    path_to_file = '/'.join(current_dirs.values())
                    ans = max(ans, len(path_to_file))
            else:
                break
        print(ans)
        return ans
s = Solution()
# s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
# s.lengthLongestPath("a.txt")
s.lengthLongestPath("a\n\taa\n\t\taaa\n\t\t\tfile1.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png")