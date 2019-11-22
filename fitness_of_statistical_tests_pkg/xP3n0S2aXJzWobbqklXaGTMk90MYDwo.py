#!/usr/bin/env
import datetime;import os;import sys;import threading;import timeit;from PyQt5 import QtWidgets;from PyQt5.QtCore import QObject, pyqtSignal;from statsmodels.stats.diagnostic import kstest_normal;import scipy;sys.path.append(






                                                                                                                                                                                os.path.dirname(






                                                                                                                                                                                    os.path.dirname(






                                                                                                                                                                                        os.path.realpath(






                                                                                                                                                                                            __file__











                                                                                                                                                                                                                                                                                                            )











                                                                                                                                                                                                                                                                                                        )











                                                                                                                                                                                                                                                                                                    )





                                                                                               





                                                                                                                );from fitness_of_statistical_tests_pkg.xkOp5RAl8sUZsplYwTqaTggzxmLNazZ import * ;from fitness_of_statistical_tests_pkg.xGmpbPMfbsBXVGeiwx4HO6yDZLhv1xU import *;from fitness_of_statistical_tests_pkg.xzNJHoYfjoBa5gtRhNAyo20ZB3rAfMK import *;from fitness_of_statistical_tests_pkg.xh07xaWPkUX3yak02uqgioCM5W7LvMN import *

class xs7TV0seFoQwRBoVUh6lNHRXuLYlTlR(






                                                                                                                                                                                QObject











                                                                                                                                                                                                                                                                                                ):

    _07QSbRLKTMosrwE5AFQvvXzDoCUnQ8 = pyqtSignal(






                                                                                                                                                                                    str, str











                                                                                                                                                                                                                                                                                                    )
    _ypBlpDpn7ljM6v3TNn8ZT0xysyVLAv = pyqtSignal(


















                                                                                                                                                                                                                                                                                                    )
    _p1hWeIJ3q1MTMc353mxX5DheMgr6ia = pyqtSignal(






                                                                                                                                                                                    str











                                                                                                                                                                                                                                                                                                    )

    def __init__(






                                                                                                                                                                                    self, ui











                                                                                                                                                                                                                                                                                                    ):
        super(






                                                                                                                                                                                        xs7TV0seFoQwRBoVUh6lNHRXuLYlTlR, self











                                                                                                                                                                                                                                                                                                        ).__init__(


















                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR = ui
        self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH = dict(


















                                                                                                                                                                                                                                                                                                        )
        self._mY8c8jt3U92RlCaE8vP4XYXgG90aLt = dict(


















                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._mxFUsVLlnbD2x25IEu0Haab4IZTnMR.clicked.connect(






                                                                                                                                                                                        self._mZa4ugcZuKx90bThWZKz4JixSS1YK2











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W.clicked.connect(






                                                                                                                                                                                        self._3UvE3Zu7o9UwgiFvgeNbf3tt5OiBni











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.selectionModel(


















                                                                                                                                                                                                                                                                                                        ).currentChanged.connect(






                                                                                                                                                                                        self._y1R0JPbz39kEjy4mTSh6vBSDDob9ev











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.selectionModel(


















                                                                                                                                                                                                                                                                                                        ).currentChanged.connect(






                                                                                                                                                                                        self._Hnh8sAmRIM8HpVDpsvWq9oUj9ynQ55











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._JJDsOStF6pGh9hsjtpj5tmSKwNuxPJ.clicked.connect(






                                                                                                                                                                                        self._0iqU6KeNF5LBlYyMaMQ52UPVvyHoWl











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._Y9rHCErysNrS9gho4uwKEBLey6qhh3.clicked.connect(






                                                                                                                                                                                        self._gy69c5tBVeXYKg0awmmcYQgfSL3hYc











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._EPPIJvylTr1KH2YZ870CJ85n1rQTA6.clicked.connect(






                                                                                                                                                                                        self._E1TsXDj4opQWDRt8vGnyzV0XwhYNGi











                                                                                                                                                                                                                                                                                                        )
        self._p1hWeIJ3q1MTMc353mxX5DheMgr6ia.connect(






                                                                                                                                                                                        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR.runtime.setText











                                                                                                                                                                                                                                                                                                        )
        self._ypBlpDpn7ljM6v3TNn8ZT0xysyVLAv.connect(






                                                                                                                                                                                        self._PnaZqlGIqPnaE9r3nCCXpE3p7rm53Q











                                                                                                                                                                                                                                                                                                        )
        self._07QSbRLKTMosrwE5AFQvvXzDoCUnQ8.connect(






                                                                                                                                                                                        self._r7WriCRzxBTaDTSNnQ95Omb42EZhFK











                                                                                                                                                                                                                                                                                                        )

    def _E1TsXDj4opQWDRt8vGnyzV0XwhYNGi(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._W5Ao0lqLYsswwargntPEK3NUIszIKp.setCurrentIndex(






                                                                                                                                                                                        1











                                                                                                                                                                                                                                                                                                        )

    def _gy69c5tBVeXYKg0awmmcYQgfSL3hYc(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._W5Ao0lqLYsswwargntPEK3NUIszIKp.setCurrentIndex(






                                                                                                                                                                                        0











                                                                                                                                                                                                                                                                                                        )

    def _H5BkWqrO1zO8VSABHF7eCKAEAgs2PK(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        self._mlVyFxOCGyPcB3nkQVmV7Lf0D8kI3L = ximqoP7GjZpiLc2jtevhq5zWKiDsbUY(


















                                                                                                                                                                                                                                                                                                        )
        self._mlVyFxOCGyPcB3nkQVmV7Lf0D8kI3L.show(


















                                                                                                                                                                                                                                                                                                        )

    def _mZa4ugcZuKx90bThWZKz4JixSS1YK2(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        _NRw44IiiNKovFYtcGiB1clpguM8yDZ = QtWidgets.QFileDialog.getOpenFileName(


















                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._YxKtsZbMTmG34Ny3YANp0byCrksUmV.setText(






                                                                                                                                                                                        _NRw44IiiNKovFYtcGiB1clpguM8yDZ[0]











                                                                                                                                                                                                                                                                                                        )

    def _3UvE3Zu7o9UwgiFvgeNbf3tt5OiBni(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        _NRw44IiiNKovFYtcGiB1clpguM8yDZ = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._YxKtsZbMTmG34Ny3YANp0byCrksUmV.text(


















                                                                                                                                                                                                                                                                                                        )
        if self._HMQWcQ8GuCb9rVYbohs1Hb4t9lM5oq(






                                                                                                                                                                                        _NRw44IiiNKovFYtcGiB1clpguM8yDZ











                                                                                                                                                                                                                                                                                                        ):
            self._EPQH9uHnbCxV76MisGOmnpADSFSpaa(


















                                                                                                                                                                                                                                                                                                            )
            if self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.layout(


















                                                                                                                                                                                                                                                                                                            ).count(


















                                                                                                                                                                                                                                                                                                            ):
                self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.layout(


















                                                                                                                                                                                                                                                                                                                ).itemAt(






                                                                                                                                                                                                0











                                                                                                                                                                                                                                                                                                                ).widget(


















                                                                                                                                                                                                                                                                                                                ).setParent(






                                                                                                                                                                                                None











                                                                                                                                                                                                                                                                                                                ) 
            self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W.setEnabled(






                                                                                                                                                                                            False











                                                                                                                                                                                                                                                                                                            )
            _Z6jpT088MuTnU5AKNTAF4KgP5RmVK2 = threading.Thread(






                                                                                                                                                                                            target=self._7cFHNbwUsaASseANLwKMkGQVpuU9Yy











                                                                                                                                                                                                                                                                                                            )
            _Z6jpT088MuTnU5AKNTAF4KgP5RmVK2.setDaemon(






                                                                                                                                                                                            True











                                                                                                                                                                                                                                                                                                            )
            _Z6jpT088MuTnU5AKNTAF4KgP5RmVK2.start(


















                                                                                                                                                                                                                                                                                                            )

    def _y1R0JPbz39kEjy4mTSh6vBSDDob9ev(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                   ):
        if self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.currentItem(




































        												):














































































        	self._IPZSPsxbzj2haC6hCxNYaFe0KmBT2K(


















                                                                                                                                                                                                                                                                                                        )
        	self._uha4zImFYS2GiABrKkvj9rtVhEHSOn(


















                                                                                                                                                                                                                                                                                                        )
        	self._ynrHRZGEfv8DEgHtoQOlleVf9nw6sc(


















                                                                                                                                                                                                                                                                                                        )
        	self._C1x0TcJZBKbnrFx5XFHN6IYjKrmA8v(


















                                                                                                                                                                                                                                                                                                        )
        	self._HzpNQsaa1NTzeKxQuex3qJ9W5PRGhu(


















                                                                                                                                                                                                                                                                                                        )

    def _Hnh8sAmRIM8HpVDpsvWq9oUj9ynQ55(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        if self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.currentItem(

















































        	):
        	







































































        	self._IPZSPsxbzj2haC6hCxNYaFe0KmBT2K(


















                                                                                                                                                                                                                                                                                                        )
        	self._uha4zImFYS2GiABrKkvj9rtVhEHSOn(


















                                                                                                                                                                                                                                                                                                        )
        	self._KC0yZP6gvIcC3XN15xyeOjWVzn6GKF(


















                                                                                                                                                                                                                                                                                                        )
        	self._kaiS1qh42XTRLj2rw9QZ04nvtmSWYn(


















                                                                                                                                                                                                                                                                                                        )
        	self._ikNqRVkOyhq5ShbgZfS8F0cplInesB(


















                                                                                                                                                                                                                                                                                                        )

    def _0iqU6KeNF5LBlYyMaMQ52UPVvyHoWl(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        self._IPZSPsxbzj2haC6hCxNYaFe0KmBT2K(


















                                                                                                                                                                                                                                                                                                        )

    def _EPQH9uHnbCxV76MisGOmnpADSFSpaa(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.clear(


















                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._HVsftfRMgBaF4sSvwYahurWCWsAGTZ.setText(






                                                                                                                                                                                        '0'











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._aEmZNzEK4eVKWLWzEXYey2zEnKabvx.setText(






                                                                                                                                                                                        '0'











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.clear(


















                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.setText(






                                                                                                                                                                                        '0'











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.setText(






                                                                                                                                                                                        'n/a'











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.setText(






                                                                                                                                                                                        '0'











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._lIpvKybBa8gWPAuTgmQnMgosnnhq5N.setText(






                                                                                                                                                                                        '0'











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._RfCmozGiipoJvcsqsfRaW2iexSYNJ5.setText(






                                                                                                                                                                                        'n/a'











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.setText(






                                                                                                                                                                                        '0'











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD.setText(






                                                                                                                                                                                        '0'











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99.setText(






                                                                                                                                                                                        '0'











                                                                                                                                                                                                                                                                                                        )

    def _7cFHNbwUsaASseANLwKMkGQVpuU9Yy(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        try:
            _U2iawqPDYesqBwDcRUumvLJ1fL6Hig = timeit.default_timer(


















                                                                                                                                                                                                                                                                                                            )
            _NRw44IiiNKovFYtcGiB1clpguM8yDZ = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._YxKtsZbMTmG34Ny3YANp0byCrksUmV.text(


















                                                                                                                                                                                                                                                                                                            )
            self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH = self._XosCkRhAEpaZ0iIFTCRblrQjERHlVU(






                                                                                                                                                                                            _NRw44IiiNKovFYtcGiB1clpguM8yDZ











                                                                                                                                                                                                                                                                                                            )
            self._mNBr95b482E07rILKkcSXuKj9CXckb = self._uMBMZA0YeHrCX3kOwyR2exyNbuQRHs(






                                                                                                                                                                                            _NRw44IiiNKovFYtcGiB1clpguM8yDZ











                                                                                                                                                                                                                                                                                                            )
            _EBzQziXsnDMZgzW48qPfNlJrG8DgBb = umrOZU13WStRuwAb7yjy74py4P9nDW(






                                                                                                                                                                                            self._mNBr95b482E07rILKkcSXuKj9CXckb











                                                                                                                                                                                                                                                                                                            )
            self._czWYU1ltzb6xNTEXlN78HjkPrsrALw(






                                                                                                                                                                                            _EBzQziXsnDMZgzW48qPfNlJrG8DgBb











                                                                                                                                                                                                                                                                                                            )
            self._beJVwcu99Z8Nug1EnRGz3MPFo1FCU4(


















                                                                                                                                                                                                                                                                                                            )
            for _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 in self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH:
                self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.addItem(






                                                                                                                                                                                                _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1











                                                                                                                                                                                                                                                                                                                )
                self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.addItem(






                                                                                                                                                                                                _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1











                                                                                                                                                                                                                                                                                                                )
            _frfDZjSnMkx4uh4AmRGWtSXewJuP4W = timeit.default_timer(


















                                                                                                                                                                                                                                                                                                            )
            _RW5vTkRlVmWjyFzzXwCIvkNzk7BCtL = (






                                                                                                                                                                                            _frfDZjSnMkx4uh4AmRGWtSXewJuP4W-_U2iawqPDYesqBwDcRUumvLJ1fL6Hig











                                                                                                                                                                                                                                                                                                            ) * 1000.0 % 1000
            _VKEgb8fI4kEQUAptSX793EkCV1fXCB, _NpFSSRQSPIqP6yZNt1CayyqaX1EDVU = divmod(






                                                                                                                                                                                            _frfDZjSnMkx4uh4AmRGWtSXewJuP4W-_U2iawqPDYesqBwDcRUumvLJ1fL6Hig, 60











                                                                                                                                                                                                                                                                                                            )
            _K7HVUzAlkSr9QOpMklaPSBUIpFhCRY, _VKEgb8fI4kEQUAptSX793EkCV1fXCB = divmod(






                                                                                                                                                                                            _VKEgb8fI4kEQUAptSX793EkCV1fXCB, 60











                                                                                                                                                                                                                                                                                                            )
            _nDbMNakoXer9NRACzKUXpOEfPZomnX =  "%dh %02dm %02ds %03dms " % (






                                                                                                                                                                                            _K7HVUzAlkSr9QOpMklaPSBUIpFhCRY, _VKEgb8fI4kEQUAptSX793EkCV1fXCB, _NpFSSRQSPIqP6yZNt1CayyqaX1EDVU, _RW5vTkRlVmWjyFzzXwCIvkNzk7BCtL











                                                                                                                                                                                                                                                                                                            )
            self._p1hWeIJ3q1MTMc353mxX5DheMgr6ia.emit(






                                                                                                                                                                                            _nDbMNakoXer9NRACzKUXpOEfPZomnX











                                                                                                                                                                                                                                                                                                            )
            self._ocEbLZ5GU1rfutiksPQnjrx3mtL4Hv(






                                                                                                                                                                                            _nDbMNakoXer9NRACzKUXpOEfPZomnX











                                                                                                                                                                                                                                                                                                            )
        except Exception as _YkXjrU0m5xSmPPQpVHUYRljlkeWspS:
            self._07QSbRLKTMosrwE5AFQvvXzDoCUnQ8.emit(






                                                                                                                                                                                            "Unknown Exception", str(






                                                                                                                                                                                                _YkXjrU0m5xSmPPQpVHUYRljlkeWspS











                                                                                                                                                                                                                                                                                                                )











                                                                                                                                                                                                                                                                                                            )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._UcCIvMaCNIWoW398NrW4cf7nVIIZ7W.setEnabled(






                                                                                                                                                                                        True











                                                                                                                                                                                                                                                                                                        )
        self._ypBlpDpn7ljM6v3TNn8ZT0xysyVLAv.emit(


















                                                                                                                                                                                                                                                                                                        )

    def _XosCkRhAEpaZ0iIFTCRblrQjERHlVU(






                                                                                                                                                                                    self, _NRw44IiiNKovFYtcGiB1clpguM8yDZ











                                                                                                                                                                                                                                                                                                    ):
        _01wb1c6wlT5hEvizkI8VCwtsu4ybFl = open(






                                                                                                                                                                                        _NRw44IiiNKovFYtcGiB1clpguM8yDZ, 'r'











                                                                                                                                                                                                                                                                                                        ).read(


















                                                                                                                                                                                                                                                                                                        ).splitlines(


















                                                                                                                                                                                                                                                                                                        )
        _fn9ImwNbPGUeJ01yoIPB8xSNPNXcOs = dict(


















                                                                                                                                                                                                                                                                                                        )
        for _SEglh3zOzEy26f2jGm9H2JpUNlOY7J in _01wb1c6wlT5hEvizkI8VCwtsu4ybFl:
            _JTzlJpleHHf6pw20xXQYyk8M970u2e = _SEglh3zOzEy26f2jGm9H2JpUNlOY7J.split(


















                                                                                                                                                                                                                                                                                                            )
            _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 = _JTzlJpleHHf6pw20xXQYyk8M970u2e[0]
            _bc9o8FSBuugZ0BrtkXF1ub9J8caaTC = [float(






                                                                                                                                                                                            _hqqPRVqu2C21D9aS9ToqbikBR4GP73











                                                                                                                                                                                                                                                                                                            ) for _hqqPRVqu2C21D9aS9ToqbikBR4GP73 in _JTzlJpleHHf6pw20xXQYyk8M970u2e[1:]]
            _fn9ImwNbPGUeJ01yoIPB8xSNPNXcOs[_rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1] = _bc9o8FSBuugZ0BrtkXF1ub9J8caaTC
        return _fn9ImwNbPGUeJ01yoIPB8xSNPNXcOs

    def _uMBMZA0YeHrCX3kOwyR2exyNbuQRHs(






                                                                                                                                                                                    self, _NRw44IiiNKovFYtcGiB1clpguM8yDZ











                                                                                                                                                                                                                                                                                                    ):
        _01wb1c6wlT5hEvizkI8VCwtsu4ybFl = open(






                                                                                                                                                                                        _NRw44IiiNKovFYtcGiB1clpguM8yDZ, 'r'











                                                                                                                                                                                                                                                                                                        ).read(


















                                                                                                                                                                                                                                                                                                        ).splitlines(


















                                                                                                                                                                                                                                                                                                        )
        _y2Ej6yT0wQWcXxFfSmuPYlfSGUQbhy = []
        with open(






                                                                                                                                                                                        _NRw44IiiNKovFYtcGiB1clpguM8yDZ, 'r'











                                                                                                                                                                                                                                                                                                        ) as _mhf20q4IMIubyjAJQDqQazIDeIBHbU:
            _gfQ1GXyWZD2uWLPmfiHYpBUjegSI9E = _mhf20q4IMIubyjAJQDqQazIDeIBHbU.read(


















                                                                                                                                                                                                                                                                                                            ).splitlines(


















                                                                                                                                                                                                                                                                                                            )
            for _SEglh3zOzEy26f2jGm9H2JpUNlOY7J in _gfQ1GXyWZD2uWLPmfiHYpBUjegSI9E:
                _JTzlJpleHHf6pw20xXQYyk8M970u2e = _SEglh3zOzEy26f2jGm9H2JpUNlOY7J.split(


















                                                                                                                                                                                                                                                                                                                )
                _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 = _JTzlJpleHHf6pw20xXQYyk8M970u2e[0]
                _bc9o8FSBuugZ0BrtkXF1ub9J8caaTC = [float(






                                                                                                                                                                                                _hqqPRVqu2C21D9aS9ToqbikBR4GP73











                                                                                                                                                                                                                                                                                                                ) for _hqqPRVqu2C21D9aS9ToqbikBR4GP73 in _JTzlJpleHHf6pw20xXQYyk8M970u2e[1:]]
                _y2Ej6yT0wQWcXxFfSmuPYlfSGUQbhy.append(






                                                                                                                                                                                                (






                                                                                                                                                                                                    _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1, _bc9o8FSBuugZ0BrtkXF1ub9J8caaTC











                                                                                                                                                                                                                                                                                                                    )











                                                                                                                                                                                                                                                                                                                )
        return _y2Ej6yT0wQWcXxFfSmuPYlfSGUQbhy


    def _czWYU1ltzb6xNTEXlN78HjkPrsrALw(






                                                                                                                                                                                    self, _EBzQziXsnDMZgzW48qPfNlJrG8DgBb











                                                                                                                                                                                                                                                                                                    ):
        _G5nDQKeAqWX7CUrCMOyEWIJ3QKFi2F = 0
        _tv3O5iZrc7LHIQ6HK2YgHkVLaS0Ojj = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR.scottknott_table
        for _WUHN8UBcDU8OJ0I0Yw71vCaxDBXrQ8 in _EBzQziXsnDMZgzW48qPfNlJrG8DgBb:
            _tv3O5iZrc7LHIQ6HK2YgHkVLaS0Ojj.insertRow(






                                                                                                                                                                                            _G5nDQKeAqWX7CUrCMOyEWIJ3QKFi2F











                                                                                                                                                                                                                                                                                                            )
            _tv3O5iZrc7LHIQ6HK2YgHkVLaS0Ojj.setItem(






                                                                                                                                                                                            _G5nDQKeAqWX7CUrCMOyEWIJ3QKFi2F, 0, QtWidgets.QTableWidgetItem(






                                                                                                                                                                                                str(






                                                                                                                                                                                                    _WUHN8UBcDU8OJ0I0Yw71vCaxDBXrQ8.regex











                                                                                                                                                                                                                                                                                                                    )











                                                                                                                                                                                                                                                                                                                )











                                                                                                                                                                                                                                                                                                            )
            _tv3O5iZrc7LHIQ6HK2YgHkVLaS0Ojj.setItem(






                                                                                                                                                                                            _G5nDQKeAqWX7CUrCMOyEWIJ3QKFi2F, 1, QtWidgets.QTableWidgetItem(






                                                                                                                                                                                                str(






                                                                                                                                                                                                    _WUHN8UBcDU8OJ0I0Yw71vCaxDBXrQ8.mean











                                                                                                                                                                                                                                                                                                                    )











                                                                                                                                                                                                                                                                                                                )











                                                                                                                                                                                                                                                                                                            )
            _tv3O5iZrc7LHIQ6HK2YgHkVLaS0Ojj.setItem(






                                                                                                                                                                                            _G5nDQKeAqWX7CUrCMOyEWIJ3QKFi2F, 2, QtWidgets.QTableWidgetItem(






                                                                                                                                                                                                str(






                                                                                                                                                                                                    _WUHN8UBcDU8OJ0I0Yw71vCaxDBXrQ8.rank











                                                                                                                                                                                                                                                                                                                    )











                                                                                                                                                                                                                                                                                                                )











                                                                                                                                                                                                                                                                                                            )
            _G5nDQKeAqWX7CUrCMOyEWIJ3QKFi2F += 1

    def _HMQWcQ8GuCb9rVYbohs1Hb4t9lM5oq(






                                                                                                                                                                                    self, _NRw44IiiNKovFYtcGiB1clpguM8yDZ











                                                                                                                                                                                                                                                                                                    ):
        _WpEeicaJjHB5gFrVkC0gjezq18ZKsH = []
        _pkgvvRzHHhhMubbOvzPNXjzX1y38Ir = 0
        try:
            _WpEeicaJjHB5gFrVkC0gjezq18ZKsH = open(






                                                                                                                                                                                            _NRw44IiiNKovFYtcGiB1clpguM8yDZ, 'r'











                                                                                                                                                                                                                                                                                                            ).read(


















                                                                                                                                                                                                                                                                                                            ).splitlines(


















                                                                                                                                                                                                                                                                                                            )
        except FileNotFoundError:
            self._r7WriCRzxBTaDTSNnQ95Omb42EZhFK(






                                                                                                                                                                                            "File Error", "File not found"











                                                                                                                                                                                                                                                                                                            )
            return False
        for _SEglh3zOzEy26f2jGm9H2JpUNlOY7J in _WpEeicaJjHB5gFrVkC0gjezq18ZKsH:
            _pkgvvRzHHhhMubbOvzPNXjzX1y38Ir += 1
            _SEglh3zOzEy26f2jGm9H2JpUNlOY7J = _SEglh3zOzEy26f2jGm9H2JpUNlOY7J.split(


















                                                                                                                                                                                                                                                                                                            )
            if len(






                                                                                                                                                                                            _SEglh3zOzEy26f2jGm9H2JpUNlOY7J











                                                                                                                                                                                                                                                                                                            ) < 2:
                self._r7WriCRzxBTaDTSNnQ95Omb42EZhFK(






                                                                                                                                                                                                "File Error", "Line " + str(






                                                                                                                                                                                                    _pkgvvRzHHhhMubbOvzPNXjzX1y38Ir











                                                                                                                                                                                                                                                                                                                    ) + " need GWF"











                                                                                                                                                                                                                                                                                                                )
                return False
            else:
                for _hqqPRVqu2C21D9aS9ToqbikBR4GP73 in _SEglh3zOzEy26f2jGm9H2JpUNlOY7J[1:]:
                    try:
                        float(






                                                                                                                                                                                                        _hqqPRVqu2C21D9aS9ToqbikBR4GP73











                                                                                                                                                                                                                                                                                                                        )
                    except ValueError:
                        self._r7WriCRzxBTaDTSNnQ95Omb42EZhFK(






                                                                                                                                                                                                        "File Error", "Line " + str(






                                                                                                                                                                                                            _pkgvvRzHHhhMubbOvzPNXjzX1y38Ir











                                                                                                                                                                                                                                                                                                                            ) + " _hqqPRVqu2C21D9aS9ToqbikBR4GP73 not number"











                                                                                                                                                                                                                                                                                                                        )
                        return False
        return True
  
    def _ocEbLZ5GU1rfutiksPQnjrx3mtL4Hv(






                                                                                                                                                                                    self, _4LaiSvpsefYSLpamgz2YJM1W9ErJGg











                                                                                                                                                                                                                                                                                                    ):
        _q7ii0fjJCp89zNRwLj0Z0ly6tnUzsj = os.path.dirname(






                                                                                                                                                                                        os.path.realpath(






                                                                                                                                                                                            __file__











                                                                                                                                                                                                                                                                                                            )











                                                                                                                                                                                                                                                                                                        ) + '\\fitness_of_statistical_tests_runtimes.csv'
        _rNJsAo9vHVDtLn2Ui09M2wLT9nxKCx = datetime.datetime.now(


















                                                                                                                                                                                                                                                                                                        ).strftime(






                                                                                                                                                                                        "%Y-%m-%d %H:%M:%S "











                                                                                                                                                                                                                                                                                                        )
        _xvYSY7Kn5kN3kwB1Emune4OnVRFBAS = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._YxKtsZbMTmG34Ny3YANp0byCrksUmV.text(


















                                                                                                                                                                                                                                                                                                        ) 
        with open(






                                                                                                                                                                                        _q7ii0fjJCp89zNRwLj0Z0ly6tnUzsj, 'a'











                                                                                                                                                                                                                                                                                                        ) as _RQXR5vLw7KI7KBYxaLQ7MELuMPh1lH:
            _RQXR5vLw7KI7KBYxaLQ7MELuMPh1lH.write(






                                                                                                                                                                                            _rNJsAo9vHVDtLn2Ui09M2wLT9nxKCx + ',' +
                               _xvYSY7Kn5kN3kwB1Emune4OnVRFBAS + ' ,' + 
                               _4LaiSvpsefYSLpamgz2YJM1W9ErJGg + '\n'











                                                                                                                                            )

    def _IPZSPsxbzj2haC6hCxNYaFe0KmBT2K(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        if not self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.currentItem(


















                                                                                                                                                                                                                                                                                                        ) or \
            not self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.currentItem(


















                                                                                                                                                                                                                                                                                                            ):
            return
        _RevjC1aJfehfjQrAW5vpCCHSIJtwGA = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        _OApPxySGa34jUN9pBSnnRVKb9UxF9c = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        _UzID8UG54Rlcuja5muW5bf8OxIeUBz = self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH[_RevjC1aJfehfjQrAW5vpCCHSIJtwGA]  
        _KfKFeH2q7kSRJ2lEX6wuuTpECRT3eA = self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH[_OApPxySGa34jUN9pBSnnRVKb9UxF9c]  
        _YxfyfBZjnPg5T4siLuUbOVT2vsNqOA = rS3gkz4bElr2McWWtUvr28kAV8LTDr(






                                                                                                                                                                                        _UzID8UG54Rlcuja5muW5bf8OxIeUBz, _RevjC1aJfehfjQrAW5vpCCHSIJtwGA, _KfKFeH2q7kSRJ2lEX6wuuTpECRT3eA, _OApPxySGa34jUN9pBSnnRVKb9UxF9c, self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nrqL1pAu3gWRNx404rIfPJHaBx9BXm, 
            _tAWDsBsRJ2QhtnCahB6bS9P2h5GbYc=self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR.bins.value(


















                                                                                                                                                                                                                                                                                                            ), _ygaiJjXRR8bHEWqxwjFHapbvrmo85Z=10, _YLkwkyW1GDyDYaBVk456yKPCfrEPOe=10, _7ucWFWiwyWNrhrO1M3WgRWiHjjf4Qz=50











                                                                                                                            )
        
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.setContentsMargins(






                                                                                                                                                                                        1, 1, 1, 1











                                                                                                                                                                                                                                                                                                        )
        _nQ0hIButJbpXHPTAzGyCIVJxm31Yfz = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nrqL1pAu3gWRNx404rIfPJHaBx9BXm.layout(


















                                                                                                                                                                                                                                                                                                        )
        if _nQ0hIButJbpXHPTAzGyCIVJxm31Yfz.count(


















                                                                                                                                                                                                                                                                                                        ):
            _nQ0hIButJbpXHPTAzGyCIVJxm31Yfz.itemAt(






                                                                                                                                                                                            0











                                                                                                                                                                                                                                                                                                            ).widget(


















                                                                                                                                                                                                                                                                                                            ).setParent(






                                                                                                                                                                                            None











                                                                                                                                                                                                                                                                                                            ) 
        _nQ0hIButJbpXHPTAzGyCIVJxm31Yfz.addWidget(






                                                                                                                                                                                        _YxfyfBZjnPg5T4siLuUbOVT2vsNqOA











                                                                                                                                                                                                                                                                                                        )

    def _uha4zImFYS2GiABrKkvj9rtVhEHSOn(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        if not self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.currentItem(


















                                                                                                                                                                                                                                                                                                        ) or \
            not self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.currentItem(


















                                                                                                                                                                                                                                                                                                            ):
            return
        _RevjC1aJfehfjQrAW5vpCCHSIJtwGA = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        _OApPxySGa34jUN9pBSnnRVKb9UxF9c = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        _UzID8UG54Rlcuja5muW5bf8OxIeUBz = self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH[_RevjC1aJfehfjQrAW5vpCCHSIJtwGA]  
        _KfKFeH2q7kSRJ2lEX6wuuTpECRT3eA = self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH[_OApPxySGa34jUN9pBSnnRVKb9UxF9c]  
        if _UzID8UG54Rlcuja5muW5bf8OxIeUBz == _KfKFeH2q7kSRJ2lEX6wuuTpECRT3eA:
            self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99.setText(






                                                                                                                                                                                            "N/A"











                                                                                                                                                                                                                                                                                                            )
            self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._aEmZNzEK4eVKWLWzEXYey2zEnKabvx.setText(






                                                                                                                                                                                            "N/A"











                                                                                                                                                                                                                                                                                                            )
        else:            
            _7EX0u0Ene4j73T0hEspxNp2b52g1py = scipy.stats.ks_2samp(






                                                                                                                                                                                            _UzID8UG54Rlcuja5muW5bf8OxIeUBz, _KfKFeH2q7kSRJ2lEX6wuuTpECRT3eA











                                                                                                                                                                                                                                                                                                            )
            _XgRhGMAQjMleoU7uOAHcKuVIXNYcy4 = _7EX0u0Ene4j73T0hEspxNp2b52g1py[0]
            _ojXoO9vFgcbE9SYjJqbMpTuRLTTi4p = _7EX0u0Ene4j73T0hEspxNp2b52g1py[1]
            self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._6ttKm8xZyn5IVs2E3UYEK8ZhK7mF99.setText(






                                                                                                                                                                                            str(






                                                                                                                                                                                                _XgRhGMAQjMleoU7uOAHcKuVIXNYcy4











                                                                                                                                                                                                                                                                                                                )











                                                                                                                                                                                                                                                                                                            )
            self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._aEmZNzEK4eVKWLWzEXYey2zEnKabvx.setText(






                                                                                                                                                                                            str(






                                                                                                                                                                                                _ojXoO9vFgcbE9SYjJqbMpTuRLTTi4p











                                                                                                                                                                                                                                                                                                                )











                                                                                                                                                                                                                                                                                                            )

    def _C1x0TcJZBKbnrFx5XFHN6IYjKrmA8v(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        _gfQ1GXyWZD2uWLPmfiHYpBUjegSI9E = self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH[_rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1]
        _7EX0u0Ene4j73T0hEspxNp2b52g1py = kstest_normal(






                                                                                                                                                                                        _gfQ1GXyWZD2uWLPmfiHYpBUjegSI9E











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._3z91Lbqj3g133OE4g7Zp0osEK0o7qy.setText(






                                                                                                                                                                                        str(






                                                                                                                                                                                            _7EX0u0Ene4j73T0hEspxNp2b52g1py[0]











                                                                                                                                                                                                                                                                                                            )











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._zr18H0ijUB3ieyuwMp8TRNrAOYAY4L.setText(






                                                                                                                                                                                        str(






                                                                                                                                                                                            _7EX0u0Ene4j73T0hEspxNp2b52g1py[1]











                                                                                                                                                                                                                                                                                                            )











                                                                                                                                                                                                                                                                                                        )

    def _HzpNQsaa1NTzeKxQuex3qJ9W5PRGhu(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._zPLeIKaBBj9E1oruGXC2zW1sBYbZNV.setText(






                                                                                                                                                                                        self._mY8c8jt3U92RlCaE8vP4XYXgG90aLt[_rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1]











                                                                                                                                                                                                                                                                                                        )

    def _ynrHRZGEfv8DEgHtoQOlleVf9nw6sc(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._nkLW5QJXDX0FklzGW2FuIkM4UCbtYl.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        _u3sIsjEAMXGWixLUQuXWfLAzSLrqnF = self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH[_rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1]
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._uQTQphyn6n5DwvQpu9Y7ShIvIH0TY3.setText(






                                                                                                                                                                                        str(






                                                                                                                                                                                            len(






                                                                                                                                                                                                _u3sIsjEAMXGWixLUQuXWfLAzSLrqnF











                                                                                                                                                                                                                                                                                                                )











                                                                                                                                                                                                                                                                                                            )











                                                                                                                                                                                                                                                                                                        )

    def _kaiS1qh42XTRLj2rw9QZ04nvtmSWYn(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        _gfQ1GXyWZD2uWLPmfiHYpBUjegSI9E = self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH[_rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1]
        _7EX0u0Ene4j73T0hEspxNp2b52g1py = kstest_normal(






                                                                                                                                                                                        _gfQ1GXyWZD2uWLPmfiHYpBUjegSI9E











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._HVsftfRMgBaF4sSvwYahurWCWsAGTZ.setText(






                                                                                                                                                                                        str(






                                                                                                                                                                                            _7EX0u0Ene4j73T0hEspxNp2b52g1py[0]











                                                                                                                                                                                                                                                                                                            )











                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._lIpvKybBa8gWPAuTgmQnMgosnnhq5N.setText(






                                                                                                                                                                                        str(






                                                                                                                                                                                            _7EX0u0Ene4j73T0hEspxNp2b52g1py[1]











                                                                                                                                                                                                                                                                                                            )











                                                                                                                                                                                                                                                                                                        )

    def _ikNqRVkOyhq5ShbgZfS8F0cplInesB(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._RfCmozGiipoJvcsqsfRaW2iexSYNJ5.setText(






                                                                                                                                                                                        self._mY8c8jt3U92RlCaE8vP4XYXgG90aLt[_rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1]











                                                                                                                                                                                                                                                                                                        )

    def _KC0yZP6gvIcC3XN15xyeOjWVzn6GKF(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 = self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._C0xbVaTqnfwVR0xv0QIssY0cByBe1L.currentItem(


















                                                                                                                                                                                                                                                                                                        ).text(


















                                                                                                                                                                                                                                                                                                        )
        _u3sIsjEAMXGWixLUQuXWfLAzSLrqnF = self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH[_rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1]
        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR._ewVBxbWP7GZ9FVyrV2IPFLw1f5cfzD.setText(






                                                                                                                                                                                        str(






                                                                                                                                                                                            len(






                                                                                                                                                                                                _u3sIsjEAMXGWixLUQuXWfLAzSLrqnF











                                                                                                                                                                                                                                                                                                                )











                                                                                                                                                                                                                                                                                                            )











                                                                                                                                                                                                                                                                                                        )        

    def _beJVwcu99Z8Nug1EnRGz3MPFo1FCU4(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        for _rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1 in self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH:
            _gfQ1GXyWZD2uWLPmfiHYpBUjegSI9E = self._EMWP0HM9cjJk1aPJnL41nLBXq7yciH[_rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1]
            _7EX0u0Ene4j73T0hEspxNp2b52g1py = wbfWGaaK6svGyGpITX3WoqvmGa7eYF(






                                                                                                                                                                                            _gfQ1GXyWZD2uWLPmfiHYpBUjegSI9E











                                                                                                                                                                                                                                                                                                            )
            self._mY8c8jt3U92RlCaE8vP4XYXgG90aLt[_rRu4kuTlZ7Lwwsesa6Bk7ifHpA38I1] = _7EX0u0Ene4j73T0hEspxNp2b52g1py

    def _r7WriCRzxBTaDTSNnQ95Omb42EZhFK(






                                                                                                                                                                                    self, _RFA2V3LTNoxeqzKqn2C1UHzR7IiWCs, _NuDaGi7mvAQeCJZwXEHkZD5KGFJTbB











                                                                                                                                                                                                                                                                                                    ):
        _Bn649yxYwyC5IOhzPwVV4cuV5iMIGc = QtWidgets.QMessageBox.critical(






                                                                                                                                                                                        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR, _RFA2V3LTNoxeqzKqn2C1UHzR7IiWCs, _NuDaGi7mvAQeCJZwXEHkZD5KGFJTbB











                                                                                                                                                                                                                                                                                                        )

    def _PnaZqlGIqPnaE9r3nCCXpE3p7rm53Q(






                                                                                                                                                                                    self











                                                                                                                                                                                                                                                                                                    ):
        _ypBlpDpn7ljM6v3TNn8ZT0xysyVLAv = QtWidgets.QMessageBox.information(






                                                                                                                                                                                        self.x0kNq0CWaRtqOvx0OCNjeOxDx4xYULR, "Tests Successful", 
            "Click on two regular expressions to activate graphing area. Click Help for more information."











                                                                                                                            )
