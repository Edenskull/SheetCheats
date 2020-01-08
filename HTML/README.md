![Badge Language](https://img.shields.io/badge/Language-HTML-blue) ![Badge Status](https://img.shields.io/badge/Status-En%20Cours-yellow)
<p align="center" style="text-align: center;">
<img src="./HTML5_Logo.svg" alt="HTML5 Logo" height="256" />
</p>
<h1 class="text-blue" style="color: #ea8853; font-weight: 400">Cheatsheet HTML5</h1>
<hr>

## HTML5 Cheatsheet

HTML5 est la dernière version du standard HTML. Cette nouvelle version contient de nouveaux éléments, attributs, comportements et un large panel de technologie qui permettent de construire des sites et applications performants et divers.

* **Sémantique** : permets de décrire plus en détail votre contenu.
* **Connectivité** : permets de communiquer avec les serveurs d'une façon nouvelle et innovante.
* **Hors ligne et stockage** : permets de stocker des données du côté du client en locale et faire des opérations hors ligne efficacement.
* **Multimédia** : fournit une nouvelle façon de gérer les objets multimédias.
* **Graphiques 2D/3D et effets** : propose de nouvelles façons de présenter.
* **Performance et integration** : fournit une grande vitesse d'optimisation et une meilleure utilisation du matériel.
* **Accès aux appareils** : permets l'utilisation d'une variété d'appareils.
* **Habillé** : permets de créer des styles attirants et petillants.

## Modèle basique

```HTML
<!DOCTYPE html>
<html lang="en" dir="ltr">

    <head>
        <meta charset="utf-8">
        <title>Example</title>
    </head>

    <body>
		<p>Hello world!</p>
    </body>

</html>
```

## Guide

### Lien CSS

Pour plus de performance on va importer les feuilles dans le head.

On peut lier du css avec la balise style (peu recommandable) :
```HTML
<head>
	<style>
		body {
			background-color: aliceblue;
		}

		p {
			font-size: 2em;
			color: red;
		}
	</style>
</head>
```

On peut aussi lier des fichiers css externes en indiquant leur chemin :
```HTML
<head>
	<link href="/css/main.css" rel="stylesheet"> <!-- Absolu -->
	<link href="css/main.css" rel="stylesheet"> <!-- Relative -->
</head>
```

On peut lier des fichiers css par lien CDN :
```HTML
<head>
	<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet">
</head>
```

### Lien Javascript

Pour plus de performance on va importer les scripts à la fin du body.

On peut lier du javascript avec la balise script (peu recommandable) :
```HTML
<body>
	<p>Hello World!</p>

	<script type="text/javascript">
		window.alert('hello world');
	</script>
</body>
```

On peut aussi lier des fichiers js externes en indiquant leur chemin :
```HTML
<body>
	<p>Hello World!</p>

	<script type="text/javascript" src="js/main.js"></script> <!-- relative -->
	<script type="text/javascript" src="/js/main.js"></script> <!-- absolu -->
</body>
```

On peut lier des fichers js par lien CDN :
```HTML
<body>
	<p>Hello World!</p>

	<script src="https://code.jquery.com/jquery-3.4.1.min.js"
		integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
		crossorigin="anonymous"></script>
</body>
```

### Les nouvelles balises utiles

<**nav**> | Balise pouvant servir à créer une barre de navigation :
```HTML
<nav>
	<a href="#">home</a>
	<a href="#">hello</a>
	<a href="#">world</a>
	<a href="#">!</a>
</nav>
```

<**footer**> | Balise pouvant servir à créer un bas de page récurrent ou non :
```HTML
<footer>
	<span>Copyright @ Edenskull</span>
</footer>
```

<**progress**> | Balise pouvant servir à créer une barre de progression (souvent couplé avec du javascript) :
```HTML
<progress value="25" max="100">25%</progress>
```

<**source**> <**video**> <**audio**> | Balise pouvant servir à afficher des vidéos ou de l'audio sur la page) :
```HTML
<video controls width="250" height="200" muted>
    <source src="/media/examples/flower.webm" type="video/webm">
    <source src="/media/examples/flower.mp4" type="video/mp4">
    This browser does not support the HTML5 video element.
</video>
```

```HTML
<audio controls src="/media/examples/t-rex-roar.mp3">
	Your browser does not support the audio element.
</audio>
```
