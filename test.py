from unittest import TestCase
import unittest
from unittest.mock import patch
from Yandex import Yandex
import requests
from doc_filter import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, documents, directories, \
    remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, \
    show_all_docs_info, add_new_doc, secretary_program_start


class TestFunc(TestCase):
    def test_doc_existance(self):
        result = check_document_existance('2207 876234')
        self.assertEqual(result, True)



    def test_doc_owner_name(self):
        result = get_doc_owner_name('11-2')
        self.assertIsInstance(result, str)
        self.assertIn(result, get_all_doc_owners_names())



    def test_all_owners_names(self):
        result = get_all_doc_owners_names()
        self.assertIsInstance(result, set)
        for doc in documents:
            self.assertIn(doc['name'], result)


    def test_remove_doc_from_shelf(self):
        result = remove_doc_from_shelf('2207 876234')
        self.assertIsInstance(result, dict)
        for item in result.values():
            arg = '2207 876234'
            self.assertNotIn(arg, directories)


    def test_add_new_shelf(self):
        with patch('builtins.input', return_value= '7'):
            shelf_number, result = add_new_shelf(2)
            self.assertEqual(result, True)
            self.assertEqual(shelf_number, '7')
            self.assertEqual(directories['7'], [])


    def test_append_doc_to_shelf(self):
        result = append_doc_to_shelf('54543', '7')
        arg = '54543'
        self.assertIsInstance(result, dict)
        self.assertIn('7', directories)
        self.assertIn(arg, directories['7'])


    def test_delete_doc(self):
        result = delete_doc('10006')
        arg = '10006'
        self.assertIsNotNone(result, True)
        self.assertNotIn(arg, documents)


    def test_get_doc_shelf(self):
        result = get_doc_shelf('2207 876234')
        arg = '2207 876234'
        arg_2 = '11-2'
        self.assertIsInstance(result, str)
        self.assertIn(arg, directories[result])


    def test_move_doc_to_shelf(self):
        result = move_doc_to_shelf('11-2', '3')
        arg = '11-2'
        self.assertIn(arg, result['3'])
        self.assertIsInstance(result, dict)


    def test_show_all_docs_info(self):
        result = show_all_docs_info()
        self.assertIsInstance(result, list)
        for doc in documents:
            for v in doc.values():
                self.assertIn(v, result)


    def test_add_new_doc(self):
        result = add_new_doc('passport', '17-42', 'Mike Vazovski', '3')
        self.assertIn('17-42', result['3'])
        self.assertEqual('Mike Vazovski', get_doc_owner_name('17-42'))



class TestYandex(TestCase):
    def setUp(self):
        self.yandex = Yandex(token)


    def test_get_headers(self):
        self.assertIsInstance(self.yandex.get_headers(), dict)


    def test_create_folder(self):
        self.assertEqual(self.yandex.create_folder('Homework_7').status_code, 201)
        path = 'Homework_7'
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        resp = requests.get(f'{url}?path={path}', headers=self.yandex.get_headers())
        self.assertEqual(resp.status_code, 200)





if __name__ == '__main__':
    unittest.main()





