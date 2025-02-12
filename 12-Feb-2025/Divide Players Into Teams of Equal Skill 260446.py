# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        result = []

        left, right = 0, len(skill) - 1
        added = skill[left] + skill[right]
        sum = 0
        while left < right:
            if added != skill[left] + skill[right]:
                return -1
            sum += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return sum


