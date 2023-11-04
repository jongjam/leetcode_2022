from collections import deque
class Twitter:

    def __init__(self):
        self.posts = deque()
        self.following = [set() for i in range(1, 10)]

    def postTweet(self, userId, tweetId):
        self.posts.appendleft([userId, tweetId])

    def getNewsFeed(self, userId):
        count = 0
        feed = []
        i = 0
        while (count < 10) & (i < len(self.posts)):
            post_author = self.posts[i][0]
            # userId is the author
            if (post_author == userId) or (post_author in self.following[userId]) :
                count += 1
                feed.append(self.posts[i][1])
            i += 1
            
        return feed

    def follow(self, followerId, followeeId):
        if 0 <= followerId < len(self.following):
            self.following[followerId].add(followeeId)
        else :
            extended = [set() for i in range(len(self.following), followerId + 1)]
            self.following.extend(extended)

    def unfollow(self, followerId, followeeId):
         if 0 <= followerId < len(self.following):
            if followeeId in self.following[followerId] :
                self.following[followerId].remove(followeeId)
            
        
def main() :
    ob = Twitter()
    
    ob.postTweet(1, 5)
    ob.getNewsFeed(1)
    ob.follow(1, 2)
    ob.postTweet(2, 6) 
    ob.getNewsFeed(1)
    ob.unfollow(1, 2)
    ob.getNewsFeed(1)
    ob.follow(500, 1)
    
main()