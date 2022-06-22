import time
import scrapy

class SpecSpider(scrapy.Spider):
    name = 'spec'
    #allowed_domains = ['https://www.emag.ro']
    start_urls = ['https://www.emag.ro/telefoane-mobile/p1/c']
    download_delay = 5.0

    def parse(self, response):
        print('inside response---- ', response, '--------------------')
        for product in response.css('div.js-products-container.card-collection.list-view-updated.show-me-a-grid div.card-v2-info'):
            #if product has reviews
            if product.css('div.star-rating-text'):
                #parse product link to get info
                link = product.css('a::attr(href)').get()
                print(' product has reviews --------- ',link)
                yield scrapy.Request(link, self.parse_products)
            else:
                print("reviews not existing...")
            time.sleep(1)
        time.sleep(2)
        # for x in range(2,30):
        #     yield scrapy.Request(f'https://www.emag.ro/telefoane-mobile/p{x}/c', self.parse)

    def parse_products(self, response):

        print('inside parse product : ', response,'-----------------------')
        phone_brand = response.xpath("//div[@class='disclaimer-section']/p/a/text()").get().strip()

        phone_name = response.xpath("//h1[@class='page-title']/text()").get().strip()

        pprice = response.xpath("//p[@class='product-new-price']/text()").get().replace('.','')
        ppsup = response.xpath("//p[@class='product-new-price']/sup/text()").get()
        phone_price = pprice + "." + ppsup

        spec = response.xpath("//section[@class='page-section page-section-light gtm_product-page-specs']")

        ptype = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Tip telefon']/following-sibling::td/text()")
        phone_type = ptype.get().strip() if ptype else ''

        psim = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Tip SIM']/following-sibling::td/text()")
        phone_type_sim = psim.get().replace("\n"," | ").strip() if psim else ''

        pos = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Sistem de operare']/following-sibling::td/text()")
        phone_os = pos.get().strip() if pos else ''

        pproc = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Model procesor']/following-sibling::td/text()")
        phone_processor_model = pproc.get().replace("\n"," | ").strip() if pproc else ''

        pprocfreq = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Frecventa procesor']/following-sibling::td/text()")
        phone_processor_frequency = pprocfreq.get().replace("\n"," | ").strip() if pprocfreq else ''

        ptech = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Tehnologii']/following-sibling::td/text()")
        phone_technology = ptech.get().replace("\n"," | ").strip() if ptech else ''

        pconect = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Conectivitate']/following-sibling::td/text()")
        phone_conectivity = pconect.get().replace("\n"," | ").strip() if pconect else ''

        psensors = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Senzori']/following-sibling::td/text()")
        phone_sensors = psensors.get().replace("\n"," | ").strip() if psensors else ''

        pcolor = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Culoare']/following-sibling::td/text()")
        phone_color = pcolor.get().replace("\n"," | ").strip() if pcolor else ''

        pdim = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Dimensiuni']/following-sibling::td/text()")
        phone_dimensions_mm = pdim.get().replace('mm','').replace("\n"," | ").strip() if pdim else ''

        palert = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='RO-ALERT']/following-sibling::td/text()")
        phone_ro_alert = palert.get().strip() if palert else ''

        pdisplaydim = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Dimensiune ecran']/following-sibling::td/text()")
        phone_display_dimensions_inch = pdisplaydim.get().replace('inch','').replace("\n"," | ").strip() if pdisplaydim else ''

        pweight = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Greutate']/following-sibling::td/text()")
        phone_weight_g = pweight.get().replace('g','').strip() if pweight else ''

        pdisplayres = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Rezolutie (pixeli)']/following-sibling::td/text()")
        phone_display_resolution = pdisplayres.get().replace("\n"," | ").strip() if pdisplayres else ''

        pmem = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Memorie interna']/following-sibling::td/text()")
        phone_internal_memory = pmem.get().strip() if pmem else ''

        pram = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Memorie RAM']/following-sibling::td/text()")
        phone_ram_memory = pram.get().strip() if pram else ''

        pblue = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Versiune Bluetooth']/following-sibling::td/text()")
        phone_bluetooth = pblue.get().replace("\n"," | ").strip() if pblue else ''

        pwifi = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Standard Wi-Fi']/following-sibling::td/text()")
        phone_wifi = pwifi.get().replace("\n"," | ").strip() if pwifi else''

        pcams = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Numar camere']/following-sibling::td/text()")
        phone_cameras = pcams.get().strip() if pcams else ''

        pfirstcam = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Rezolutie camera principala']/following-sibling::td/text()")
        phone_first_camera = pfirstcam.get().replace("\n"," | ").strip() if pfirstcam else ''

        psecondcam = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Rezolutie camera frontala']/following-sibling::td/text()")
        phone_second_camera_mpx = psecondcam.get().replace('Mpx','').replace("\n"," | ").strip() if psecondcam else ''

        pvideo = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Rezolutie video']/following-sibling::td/text()")
        phone_video = pvideo.get().replace("\n"," | ").strip() if pvideo else ''

        pbattery = spec.xpath("//td[@class='col-xs-4 text-muted'][text()='Capacitate baterie']/following-sibling::td/text()")
        phone_battery = pbattery.get().strip() if pbattery else ''

        yield {
            'phone_name': phone_name,
            'phone_brand': phone_brand,
            'phone_type' : phone_type,
            'phone_price': phone_price,
            'phone_sim_type' : phone_type_sim,
            'phone_os' : phone_os,
            'phone_processor_model' : phone_processor_model,
            'phone_processor_frequency' : phone_processor_frequency,
            'phone_technology':phone_technology,
            'phone_conectivity':phone_conectivity,
            'phone_sensors' :phone_sensors,
            'phone_color' :phone_color,
            'phone_dimensions' :phone_dimensions_mm,
            'phone_weight_g' :phone_weight_g,
            'phone_RO_alert' :phone_ro_alert,
            'phone_display_dimension_inch' :phone_display_dimensions_inch,
            'phone_display_resolution' :phone_display_resolution,
            'phone_internal_memory' :phone_internal_memory,
            'phone_ram_memory' :phone_ram_memory,
            'phone_bluetooth' :phone_bluetooth,
            'phone_wifi' :phone_wifi,
            'phone_cameras' :phone_cameras,
            'phone_primary_camera' :phone_first_camera,
            'phone_secondary_camera':phone_second_camera_mpx,
            'phone_video' :phone_video,
            'phone_battery':phone_battery,
        }