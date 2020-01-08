![Badge Language](https://img.shields.io/badge/Language-Javascript-blue) ![Badge Status](https://img.shields.io/badge/Status-En%20Cours-yellow)
<p align="center" style="text-align: center;">
<img src="./JS_Logo.svg" alt="Javascript Logo" height="256" />
</p>
<h1 class="text-blue" style="color: #ea8853; font-weight: 400">Cheatsheet Javascript</h1>
<hr>

## Javascript Cheatsheet

JavaScript (qui est souvent abrégé en « JS ») est un langage de script léger, orienté objet, principalement connu comme le langage de script des pages web. Mais il est aussi utilisé dans de nombreux environnements extérieurs aux navigateurs web tels que Node.js, Apache CouchDB voire Adobe Acrobat. Le code JavaScript est interprété ou compilé à la volée. C'est un langage utilisant le concept de prototype, disposant d'un typage faible et dynamique qui permet de programmer suivant plusieurs paradigmes de programmation : fonctionnelle, impérative et orientée objet

## Guide

### Tableau

Création de tableau avec contenu dynamique :
```JS
var arrayEmpty = [];
var arrayNumber = [1,2,3,4,5196484];
var arrayString = ["hello", "world"];
var arrayMixt = ["hello", 12];
```

Ajouter des élements à mon tableau :
```JS
var array = [];
array.push("world"); // Ajouter l'élément à la fin du tableau
array.unshift("hello"); // Ajouter l'élément au début du tableau

>> array = ["hello","world"]
```

Supprimer des éléments de mon tableau :
```JS
var array = [1,2,3,4];
array.pop();
array.shift();
array.splice(0,1);

>> array = [3]
```
