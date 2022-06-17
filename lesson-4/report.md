1.  Был установлен PostgreSQl, заведен пользователь django_user и настроен доступ 
2.  В базу данных были добавлены следующие модели: colors, countries, descriptions, teas
    colors:
    class Colors(models.Model):
        color_id=models.BigAutoField(primary_key=True)
        name = models.TextField( blank=False,unique = True)
    (CREATE TABLE colors ( color_id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE );)

    countries:
    class Countries (models.Model):
        country_id=models.BigAutoField(primary_key=True)
        name = models.TextField( blank=False,unique = True)
    (CREATE TABLE countries ( country_id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE );)

    descriptions:
    class Descriptions (models.Model):
        description_id=models.BigAutoField(primary_key=True)
        description = models.TextField(blank=False,unique = True)
    (CREATE TABLE descriptions ( description_id SERIAL PRIMARY KEY, description TEXT  UNIQUE );)

    teas:
    class Teas (models.Model):
        tea_id=models.BigAutoField(primary_key=True)
        name = models.TextField( blank=False,unique = True)
        color = models.ForeignKey(Colors, null=True, on_delete = models.SET_NULL)
        description = models.OneToOneField(Descriptions, null=True, on_delete = models.CASCADE)
        countries = models.ManyToManyField(Countries)

    (CREATE TABLE teas ( tea_id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE, color_id INT, description_id INT, CONSTRAINT fk_colors FOREIGN KEY(color_id) REFERENCES colors(color_id), CONSTRAINT fk_descriptions FOREIGN KEY(description_id) REFERENCES descriptions(description_id) );)

    tea_country:
    (CREATE TABLE tea_country ( tea_id INT, country_id INT, PRIMARY KEY (tea_id , country_id), CONSTRAINT fk_teas FOREIGN KEY(tea_id) REFERENCES teas(tea_id), CONSTRAINT fk_countries FOREIGN KEY(country_id) REFERENCES countries(country_id) );)

    Установленыы связи:
    colors to teas - Один ко многим
    descriptions to teas - Один к одному
    countries to teas - Многие ко многим

    Были подготовлены модели и миграция.


    