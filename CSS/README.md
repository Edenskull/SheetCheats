![Badge Language](https://img.shields.io/badge/Language-CSS-blue) ![Badge Status](https://img.shields.io/badge/Status-En%20Cours-yellow)
<p align="center" style="text-align: center;">
<img src="./CSS3_Logo.svg" alt="CSS3 Logo" height="256" />
</p>
<h1 class="text-blue" style="color: #4b66ee; font-weight: 400">Cheatsheet CSS3</h1>
<hr>

## CSS3 Cheatsheet

Cascading Style Sheets (CSS) est un langage de feuille de style utilisé pour décrire la présentation d'un document écrit en HTML ou en XML. CSS décrit la façon dont les éléments doivent être affichés à l'écran, sur du papier, en vocalisation, ou sur d'autres supports.
CSS3 est la dernière version de ce language et apporte son lot de nouveautés.

## Modèle basique

```CSS
html {
  margin: 0;
  padding: 0;
}
```

## Guide

### Selection multiple

Selectionner plusieurs composants et changer leurs caracteristiques :
```CSS
h1, h2, h3, h4 {
  color: aliceblue;
}
```

### Selection précise

Ici, permet de selectionner tout les composants h3 qui sont dans une div :
```CSS
div h3 {
  color: red;
}
```

```HTML

```

Ici, permet de selectionner tout les composants qui h3 qui sont dans une div qui possède la classe ``red`` :
```CSS
div.red>h3 {
  color: yellow;
}
```
Exemple
```HTML
<div class="red">
  <h3>je suis jaune</h3>
</div>
```

Ici, permet de selectionner les composants h3 qui sont juste après une div :
```CSS
div+h3 {
  color: yellow;
}
```
Exemple :
```HTML
<div></div>
<h3>je suis jaune</h3>
```
