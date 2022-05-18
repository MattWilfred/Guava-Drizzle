from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from sklearn.tree import DecisionTreeClassifier
import joblib

import pandas as pd
from sklearn.model_selection import train_test_split
import wittgenstein as lw

# Create your models here.
class Data(models.Model):
    nitrogen = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(300)], null=True)
    phosphorus = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(300)], null=True)
    potassium = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(300)], null=True)
    temperature = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)], null=True)
    humidity = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)], null=True)
    ph = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(14)], null=True)
    rainfall = models.PositiveIntegerField(validators = [MinValueValidator(0), MaxValueValidator(400)], null=True)

    predicted_crop = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/crop_model.joblib')
        self.predicted_crop = ml_model.predict([[self.nitrogen, self.phosphorus, self.potassium, self.temperature, self.humidity, self.ph, self.rainfall]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-id']

class DataB(models.Model):
    crop = models.CharField(max_length=100, null=True)
    predicted_conditions = models.CharField(max_length=1000, blank=True)

    def save(self, *args, **kwargs):
        data = pd.read_csv("ml_model/Crop_Dataset-new.csv")

        X = data.drop(['label'], axis=1)
        y = data['label']

        X_train, X_test = train_test_split(data, test_size=.30)
        clf = lw.RIPPER()
        clf.fit(X_train, class_feat='label', pos_class=self.crop, random_state=42)
        self.predicted_conditions = clf.ruleset_.out_pretty()
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-id']

