class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []
        def backtrack(index, parts):
            remaining = len(s) - index
            slots = 4 - len(parts)
            if remaining < slots or remaining > slots * 3:
                return
            if index == len(s) and len(parts) == 4:
                result.append(".".join(parts))
                return
            for length in range(1, 4):
                piece = s[index:index + length]
                if len(piece) != length:
                    break
                if (piece.startswith("0") and length > 1) or int(piece) > 255:
                    continue
                backtrack(index + length, parts + [piece])
        backtrack(0, [])
        return result
