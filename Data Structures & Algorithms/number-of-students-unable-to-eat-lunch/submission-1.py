class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # optimal
        # order of students doesnt matter
        # order of sandwiches matter
        # but the quantity matters the most

        res = len(students)
        cnt = Counter(students)

        # counter => cnt = {}  
        #            for s in students:
        #                if s not in cnt:
        #                    cnt[s] = 0
        #                cnt[s] += 1

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res
        return res
        