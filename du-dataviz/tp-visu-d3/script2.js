/*global console,d3 */
(function () {
    "use strict";
    var         // Paramètres globaux du graphique
        marges = { haut: 20, droite: 20, bas: 30, gauche: 40},
        largeur = 1200,
        hauteur = 400,
        hauteurGraphe = hauteur - marges.bas - marges.haut,
        
        // Echelle en X et en Y
        x = d3.scale.ordinal().rangeBands([marges.gauche, largeur - marges.droite]),
        y = d3.scale.ordinal().rangeBands([marges.haut, hauteur - marges.bas]),
        
        // Echelle de couleur
        couleur = d3.scale.linear().range(["blue", "red"]),
    
        // Axes en X et en Y
        axeX = d3.svg.axis().scale(x).tickFormat(function (a) {
            if (a % 10 === 0) {
                return a;
            } else {
                return "";
            }
        }), // d3.format("")
        axeY = d3.svg.axis().scale(y).orient("left"), //.tickFormat(d3.format("")),
                
        // Graphique en lui-même
        graphe = d3.select("#heatmap").append("svg")
            .attr("width", largeur)
            .attr("height", hauteur);
    
    d3.text("HadCRUT.4.4.0.0.monthly_ns_avg.txt", function (texte) {
        var texteNouveau = texte.replace(/ {3}/g, ";"),
            donnees = d3.dsv(";", "text/plain").parseRows(texteNouveau)
                .map(function (ligne) {
                    var anmois = ligne[0].split("/");
                    return {
                        annee: +anmois[0],
                        mois: +anmois[1],
                        mediane: +ligne[1],
                        intervale1: { bas:  +ligne[2], haut:  +ligne[3]},
                        intervale2: { bas:  +ligne[4], haut:  +ligne[5]},
                        intervale3: { bas:  +ligne[6], haut:  +ligne[7]},
                        intervale4: { bas:  +ligne[8], haut:  +ligne[9]},
                        intervale5: { bas: +ligne[10], haut: +ligne[11]}
                    };
                });
        // console.log(donnees);
        
        // Définition des domaines des axes
        x.domain(Array.from({length: donnees.slice(-1)[0].annee - donnees[0].annee + 1}, function (d, i) { return (i + donnees[0].annee); }));
        y.domain(Array.from({length: 12}, function (d, i) { return (i + 1); }));
        
        // Définition du domaine des couleurs (min et max des anomalies donc)
        couleur.domain([d3.min(donnees.map(function (d) { return d.mediane; })),
                        d3.max(donnees.map(function (d) { return d.mediane; }))]);
        
        // Création des axes X et Y
        graphe.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + (hauteur - marges.bas) + ")")
            .call(axeX);
        graphe.append("g")
            .attr("class", "y axis")
            .attr("transform", "translate(" + marges.gauche + ",0)")
            .call(axeY);
        
        // Ajout des rectanges pour chaque mois et chaque année
        graphe.selectAll("rect")
            .data(donnees)
            .enter()
            .append("rect")
            .attr("x", function (d) { return x(d.annee); })
            .attr("y", function (d) { return y(d.mois); })
            .attr("width", largeur / (donnees[donnees.length - 1].annee - donnees[0].annee))
            .attr("height", y.rangeBand())
            .style("fill", function (d) { return couleur(d.mediane); });
    });

}());