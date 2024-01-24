'''https://www.codewars.com/kata/588a7d45019c42be61000009'''
# Your friend Rick is trying to send you a message, but he is concerned that it would get intercepted by his partner. He came up with a solution:
#     Add digits in random places within the message.
#     Split the resulting message in two. He wrote down every second character on one page, and the remaining ones on another. He then dispatched the two messages separately.
# Write a function interweave(s1, s2) that reverses this operation to decode his message!
# Example 1: interweave("hlo", "el") -> "hello" Example 2: interweave("h3lo", "el4") -> "hello"
# Rick's a bit peculiar about his formats. He would feel ashamed if he found out his message led to extra white spaces hanging around the edges of his message...

def interweave(s1, s2):
    s1,s2,s3=[*s1],[*s2],''
    for i in range(len(s1)+len(s2)):
        s3+=s2.pop(0) if i%2 else s1.pop(0)
    return ''.join(filter(lambda c: not c.isdigit(),[*s3]))
