# Jeu NSI

Ce projet est partagé entre plusieurs personnes. Git et GitHub permettent de conserver l'historique du code et de regrouper les modifications, mais ils ne remplacent pas une méthode de travail organisée.

L'objectif est que chacun travaille sur une version à jour, décrive clairement ses changements et envoie un projet qui fonctionne.

## Git et GitHub

- **Git** est l'outil installé sur l'ordinateur. Il suit les changements et crée des commits.
- **GitHub** héberge une copie distante du dépôt et permet de la partager.
- Le dossier sur l'ordinateur est le **dépôt local**.
- Le dépôt GitHub est le **dépôt distant**, appelé `origin` dans ce projet.

Un commit est une sauvegarde identifiée dans l'historique Git. Il n'est pas visible par les autres tant qu'il n'a pas été envoyé avec `git push`.

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

Sans `git pull`, on peut travailler sur une ancienne version. Par exemple, si ton ami modifie `main.py` et fait `git push`, ton ordinateur ne possède pas encore sa modification. Si tu modifies ensuite le même fichier et essaies de l'envoyer, Git peut refuser le `push` ou demander de résoudre un conflit.

Faire `git pull` au début permet donc de partir de la version la plus récente. Cela réduit les conflits et évite d'écraser accidentellement le travail des autres.

L'ordre des étapes est important : `pull` avant le travail, `diff` avant le commit, puis `push` après un commit testé.

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

Un commit doit correspondre à une modification cohérente. Évitez les messages vagues comme `changements` ou `test`.

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

## En cas de conflit ou de `push` refusé

Un `push` peut être refusé si une autre personne a envoyé un commit entre votre `pull` et votre `push`. Commencez par récupérer cette nouvelle version :

```bash
git pull origin main
```

Si Git signale un conflit, ouvrez les fichiers concernés et comparez les zones marquées par `<<<<<<<`, `=======` et `>>>>>>>`. Conservez les deux modifications lorsqu'elles sont compatibles, puis supprimez les marqueurs. Ensuite :

```bash
git add .
git commit -m "Résoudre le conflit"
git push origin main
```

Ne supprimez pas le travail de l'autre personne uniquement pour faire disparaître un conflit.

## Règles pour travailler efficacement à plusieurs

1. Toujours faire `git pull origin main` avant de commencer.
2. Ne pas modifier le même fichier important en même temps sans prévenir l'autre personne.
3. Faire des commits petits et compréhensibles.
4. Tester le jeu avant chaque `push`.
5. Ne jamais envoyer de mots de passe, clés privées ou fichiers inutiles.
6. Prévenir l'autre personne après un `push` important.
7. Ne pas utiliser `git push --force` sur `main` : cette commande peut effacer l'historique distant.
