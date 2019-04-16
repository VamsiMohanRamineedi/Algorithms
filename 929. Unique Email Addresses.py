# Unique email addresses - Time: O(n), space: O(numberOfUnique)
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            
            local = local.split('+')[0]
            local = local.split('.')
            local = ''.join(local)
            final = local + '@' + domain
            unique_emails.add(final)
        return len(unique_emails)