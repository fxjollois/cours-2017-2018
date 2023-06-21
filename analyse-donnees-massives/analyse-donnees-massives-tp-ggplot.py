ggplot(aes("Sepal.Length"), data=iris) + geom_histogram()
ggplot(aes("Sepal.Length"), data=iris) + geom_density()
ggplot(aes("Sepal.Length"), data=iris) +\
    geom_histogram(y = "..density..") +\
    geom_density()
