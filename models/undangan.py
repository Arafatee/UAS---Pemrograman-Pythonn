from odoo import models, fields, api, _
import datetime

class Undangan(models.Model):
    _name      = "undangan"
    _description   = "Undangan"

    date_create = fields.Char(string="Tanggal Di Buat", default="Yogyakarta, ")
    date_time   = fields.Char(string="Tanggal Pelaksanaan", required=True)
    time        = fields.Char(string="Waktu Pelaksanaan")
    tempat      = fields.Char(string="Tempat Pelaksanaan")
    keterangan  = fields.Text(string="Keterangan Acara")
    nomor       = fields.Char(string="Nomor Surat", default="005/RT/VII/", required=True)

    sah_jabatan = fields.Char(string="Pemegang Jabatan")
    sah_nama    = fields.Char(string="Nama")


    # @api.depends("warna")
    # def _compute_color(self):
    #     for record in self:
    #         record.color = 'red' if record.warna < 3 else 'green'
    
    # color = fields.Char(string="Color", conpute="_compute_color", store=True)

