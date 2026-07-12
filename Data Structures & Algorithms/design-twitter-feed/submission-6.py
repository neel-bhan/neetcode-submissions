class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append((self.time, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:

        fo = set(self.follows[userId])
        fo.add(userId)

        li = []
        for f in fo:
            li.extend(self.posts[f])

        li.sort(reverse=True)  
        return [tid for _, tid in li[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
