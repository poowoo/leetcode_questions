hash_table = []
class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.        
        :type longUrl: str
        :rtype: str
        """
        hash_table.append(longUrl)        
        return "http://tinyurl.com/" + str(hash_table.index(longUrl))                
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.        
        :type shortUrl: str
        :rtype: str
        """
        
        
        i = int(shortUrl[shortUrl.rindex("/")+1:])
        
        return hash_table[i]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))