# -*- coding: utf-8 -*-
from odoo import http, models, fields
from odoo.http import request
import json


class Delfimart(http.Controller):
    @http.route('/delfimart/get_barang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['delfimart.barang'].search([])
        isibarang = []
        for b in barang:
            isibarang.append({
                'nama_barang' : b.name,
                'harga_beli' : b.harga_beli,
                'harga_jual' : b.harga_jual
            })
        return json.dumps(isibarang)

    @http.route('/delfimart/get_produk', auth='public', method=['GET'])
    def getProduk(self, **kw):
        prod = request.env['delfimart.produk'].search([])
        isiproduk = []
        for p in prod:
            isiproduk.append({
                'nama_produk' : p.name,
                'kode_produk' : p.nomor_kode_produk
            })
        return json.dumps(isiproduk)

    