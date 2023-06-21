barplot(res$eig[,2], names.arg = 1:nrow(res$eig))
drawn <-
c("37", "35", "44", "28", "39", "53", "23", "45", "32", "15", 
"38", "47", "4", "14", "20", "51", "2", "6", "26", "29")
plot.MCA(res, select = drawn, axes = 1:2, choix = 'ind', invisible = c('var', 'quali'), title = '', cex = cex)
drawn <-
c("Abdo_y", "Abdo_n", "Fever_n", "Fever_y", "Diarrhea_n", "Diarrhea_y", 
"Vomit_n", "Vomit_y")
plot.MCA(res, selectMod = drawn, axes = 1:2, choix = 'ind', invisible = 'ind', title = '', cex = cex)
res.hcpc = HCPC(res, nb.clust = -1, graph = FALSE)
drawn <-
c("37", "35", "44", "28", "39", "53", "23", "45", "32", "15", 
"38", "47", "4", "14", "20", "51", "2", "6", "26", "29")
plot.HCPC(res.hcpc, choice = 'map', draw.tree = FALSE, select = drawn, title = '')
dimdesc(res, axes = 1:1)
res.hcpc$desc.var
