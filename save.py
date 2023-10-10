import yaml
import os

class DataStructure():
    def __init__(self):
        self.scores = {}
        self.name = ''
        self.load_data()

    def __str__(self):
        """Вывод данных при принте"""
        result = f'\nИмя = {self.name}\nРекорды:\n'
        for k,v in self.scores.items():
            result += f'{k} = {v}'
        return result

    def get_data(self):
        """Возвращает данные"""
        return self.scores, self.name

    def get_score(self, game):
        if game in self.scores.keys():
            return self.scores[game]
        else:
            return 0

    def put_data(self,  reverse=False, **data):
        """Передача новых данных"""
        for k, v in data.items():
            if k == 'name':
                self.name = v
            elif k == 'scores':
                self.scores = v
            else:
                if k in self.scores.keys():
                    if not reverse:
                        if v > self.scores[k]:
                            self.scores[k] = v
                    else:
                        if v < self.scores[k]:
                            self.scores[k] = v
                else:
                    self.scores[k] = v


    def save(self):
        """Сохранение данных в файл"""
        with open('data.yaml', 'w', encoding='utf-8') as data_file:
            data = {
                'scores': self.scores,
                'name': self.name
            }
            yaml.dump(data, data_file)

    def load_data(self):
        """Загрузка данных"""
        if os.path.exists('data.yaml'):
            with open('data.yaml', 'r', encoding='utf-8') as data_file:
                data = yaml.load(data_file, Loader=yaml.FullLoader)
                self.scores = data['scores']
                self.name = data['name']