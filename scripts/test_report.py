# -*- coding: utf-8 -*-
class TestReport:
    def test_report1(self):
        print(123)
        assert 1
    def test_report2(self):
        print(123)
        assert 0   
    def test_report3(self):
        print(123)
        assert 1
    def test_report4(self):
        assert 0
