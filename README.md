# Projet 5ANIM

## Génération des images

### Chargement du modèle
`bash ./scripts/download_pix2pix_model.sh facades_label2photo`

### Chargement du dataset
`bash ./datasets/download_pix2pix_dataset.sh facades`

### Application du modèle sur le dataset
`python test.py --dataroot ./datasets/facades/ --direction BtoA --model pix2pix --name facades_label2photo_pretrained`

## Visualisation des résultats

Dans le dossier `pytorch-CycleGAN-and-pix2pix/results`, il y aura un `index.html` ouvrable dans le navigateur

## Animations des résultats

### Exécution 
`python main.py` pour créer les animations dans le dossier `animations`
