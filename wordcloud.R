library(tm)
library(wordcloud)

removeUnicode <- function(x){gsub("\u0092","'",x)}

words <- Corpus(DirSource("lyrics/"))

words <- tm_map(words, stripWhitespace)
words <- tm_map(words, tolower)


words <- tm_map(words, removeUnicode)
words <- tm_map(words, removeWords, grep("'", stopwords("english"), value=TRUE))
words <- tm_map(words, removeWords, stopwords("english"))
words <- tm_map(words, removePunctuation)

#words <- tm_map(words, stemDocument)
words <- tm_map(words, PlainTextDocument)

png(filename="wordcloud.png", width = 500, height = 500)
wordcloud(words, scale=c(7,0.7), 
          max.words=50, random.order=FALSE, 
          rot.per=0.25, use.r.layout=FALSE, 
          colors=brewer.pal(8, "Dark2"))
dev.off()

wordCounts <- as.data.frame(as.matrix(TermDocumentMatrix(words)))
wordCounts["time",]


