# Leetcode Link: https://leetcode.com/problems/design-twitter/
# **************** Python Solution ***********************
# ---------- Question ----------
# Design a simplified Twitter: postTweet, getNewsFeed (10 most recent from self + followees),
# follow, unfollow.
# ---------- Approach ----------
# Hash maps for tweets and follows. Min-heap merge for news feed (like merge k sorted lists).
# Time: O(k log k) for getNewsFeed where k = followees | Space: O(n)
import heapq
from collections import defaultdict
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1  # Negative for min-heap (most recent first)
    def getNewsFeed(self, userId: int):
        heap = []
        self.following[userId].add(userId)
        for fid in self.following[userId]:
            if fid in self.tweets:
                idx = len(self.tweets[fid]) - 1
                t, tid = self.tweets[fid][idx]
                heapq.heappush(heap, (t, tid, fid, idx))
        feed = []
        while heap and len(feed) < 10:
            t, tid, fid, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:
                t2, tid2 = self.tweets[fid][idx - 1]
                heapq.heappush(heap, (t2, tid2, fid, idx - 1))
        return feed
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
