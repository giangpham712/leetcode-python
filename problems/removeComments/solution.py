from typing import List


class Solution:
    def solve(self, source: List[str]) -> List[str]:
        result = []
        isInComment = False
        currentLine = ""
        endLine = False
        for line in source:

            print(line, "")

            while line != "":
                if not isInComment:
                    commentBlockStartIndex = line.find("/*")
                    lineCommentIndex = line.find("//")
                    if lineCommentIndex != -1 and (lineCommentIndex < commentBlockStartIndex or commentBlockStartIndex == -1):
                        currentLine += line[:line.find("//")]
                        endLine = True
                        break

                    commentBlockStartIndex = line.find("/*")
                    if commentBlockStartIndex != -1:
                        isInComment = True
                        currentLine += line[:commentBlockStartIndex]
                        line = line[commentBlockStartIndex+2:]
                        continue
                    else:
                        currentLine += line[:]
                        line = ""
                        continue

                if isInComment:
                    commentBlockEndIndex = line.find("*/")
                    if commentBlockEndIndex != -1:
                        isInComment = False
                        line = line[commentBlockEndIndex+2:]
                        continue
                    else:
                        line = ""


            if not isInComment or endLine:
                result.append(currentLine)
                currentLine = ""
                endLine = False

        return list(filter(None, result))
