# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name" : "Purchase Order Tender Portal",
    "author" : "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Portal",
    "summary": "Manage Multiple Tenders, Multiple Tender Single List Module, Purchase Tender Management, PO Tender Management, Manage Multiple RFQs, Vendor Change RFQ Price, Manage Po Tender Price, Client Change RFQ Price ,Supplier Change Quotation Price app Odoo",
    "description": """
    Nowadays in a competitive market, several vendors sell the same products and everyone has their price so it will difficult to manage multiple tenders list at a time even in odoo there is no kind of feature where you can manage multiple tenders & RFQ's in a single list. Here the vendor can change the price from portal or website for tenders & RFQ's. Changed price automatically updates in odoo backend. Using this module you can easily confirm, cancel tender RFQs. This module provides many stages for manage tender like Draft, Confirm, Bid Selection, Close, Cancel, etc. You can easily send a tender pdf report to your partner's email.
 Tender Management - Portal Odoo, RFQ - Portal Odoo, PO Tender Management Odoo
 
 Manage Multiple Tenders In Single List Module, Request For Quotation Multiple Tenders  Manage, Purchase Tender Management, Manage Multiple RFQs, Manage Po Tender Price, Request For Quote Update Price, Client Change RFQ Price ,Supplier Change Quotation Price, Manage Multiple Tenders, Manage Tender Price Odoo.
 
 Manage Multiple Tenders, Multiple Tender  Single List Module, Multiple Tenders Request For Quotation Manage App, Purchase Tender Management, PO Tender Management, Manage Multiple RFQs, Vendor Change RFQ Price App, Manage Po Tender Price, Client Change RFQ Price ,Supplier Change Quotation Price, Manage Tender Price Odoo.


                    """,
    "version":"13.0.7",
    "depends" : ["base","sh_po_tender_management","sh_rfq_portal"],
    "application" : True,
    "data" : [
            'security/ir.model.access.csv',
            'views/tender_portal_template_view.xml',
            'views/tender_rfq_portal_view.xml',
            ],
    "images": ["static/description/background.png", ],
    "auto_install":False,
    "installable" : True,
    "price": 100,
    "currency": "EUR"
}
