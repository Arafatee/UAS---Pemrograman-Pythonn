from odoo import models, fields, api, _

class rismu(models.Model):
    _name = "rismu"
    _description = "RISMU"

    date_create = fields.Char(string="Tanggal Di Buat", default="Yogyakarta, ")
    date_time   = fields.Char(string="Tanggal Pelaksanaan", required=True)
    time        = fields.Char(string="Waktu Pelaksanaan")
    tempat      = fields.Char(string="Tempat Pelaksanaan")
    keterangan  = fields.Char(string="Keterangan Acara")
    
    nomor       = fields.Char(string="Nomor Surat", default="001/RISMU/", required=True)
    