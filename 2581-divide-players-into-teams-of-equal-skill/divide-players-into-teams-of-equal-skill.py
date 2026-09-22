class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        '''
        given positive integer array skill of even length n where 
        skill[i] denotes the skiill of the ith player.
        Divide the players such that the total skill of each team is equal

        the chemistry of a team is equal to the product of the skills of the players on the team
        return the sum of the chemistry of all the teams
        or return -1 if no way

        '''
        total_teams = len(skill) // 2
        skill.sort()
        chemistry = 0
        product = 1
        l, r = 0, len(skill) - 1
        skill_level = skill[-1] + skill[0]
        while total_teams and l < len(skill) and r >= 0:
            if skill[r] + skill[l] != skill_level:
                return -1
            product = skill[r] * skill[l]
            chemistry += product
            total_teams -= 1
            l += 1
            r -= 1
        if total_teams == 0: return chemistry
        return -1