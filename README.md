# Jeu NSI

Ce fichier explique comment envoyer les modifications du projet vers GitHub.

## Récupérer le projet

La première fois, clonez le dépôt :

```bash
git clone https://github.com/victormaintier03-ctrl/jeux-.git
cd jeux-
```

`git clone` télécharge le projet. `cd jeux-` entre dans son dossier.

## Récupérer les dernières modifications

Avant de travailler, utilisez :

```bash
git pull origin main
```

Cette commande récupère les changements envoyés par les autres membres.

## Vérifier les fichiers modifiés

Après avoir modifié le code ou les assets :

```bash
git status
```

Cette commande indique les fichiers nouveaux, modifiés ou supprimés.

## Préparer les modifications

```bash
git add .
```

Le point `.` signifie « tous les fichiers du dossier actuel ».

## Créer un commit

Un commit enregistre les modifications localement :

```bash
git commit -m "Décrire les modifications"
```

Exemple :

```bash
git commit -m "Corriger les chemins des assets"
```

## Envoyer les modifications sur GitHub

```bash
git push origin main
```

`git push` envoie les commits vers GitHub. `origin` désigne le dépôt distant et `main` la branche principale.

## Routine complète

```bash
git pull origin main
git status
git add .
git commit -m "Décrire les modifications"
git push origin main
```

## Première configuration de Git

Si Git demande votre identité, configurez vos informations :

```bash
git config --global user.name "Votre nom"
git config --global user.email "votre@email.com"
```

## En cas de conflit

Si `git pull` signale un conflit, ouvrez les fichiers concernés et choisissez la bonne version. Ensuite :

```bash
git add .
git commit -m "Résoudre le conflit"
git push origin main
```

Faites un `git pull` avant de commencer et utilisez des messages de commit clairs.
