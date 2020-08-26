<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content" id="pdfContent">
      <breadcumb :page=this.templates.txtInspectionTemplateName :folder="'Inspection'" />
      <div class="row mb-4">
        <b-col md="4">
          <b-input-group size="" prepend="Inspection Number">
            <b-form-input v-model="this.InspectionNumber"></b-form-input>
          </b-input-group>
        </b-col>
      </div>

      <!-- DEVICE MODEL -->
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-body p-0">
              <h5 class="card-title p-3 pb-0 mb-0">Device Model</h5>
              <b-row class="mr-3 p-3 pt-0">
                <b-col md="12" class="mt-3">
                  <b-form-select id="select-1" v-model="selDevice" :options="optionsDeviceModel" @change="onDeviceChange($event)" required
                    value-field="id" text-field="txtSerialNumber"> </b-form-select>
                </b-col>
              </b-row>
              <b-row class="mr-3 p-3 pt-0">
                <b-col md="4">
                  <h5>Manufacturer</h5>
                  <p  class="mb-0">{{ this.Manufacturer }}</p>
                </b-col>
                <b-col md="4">
                  <h5>Supplier</h5>
                  <p  class="mb-0">{{ this.Supplier }}</p>
                  </b-col>
                <b-col md="4">
                  <h5>Device Model</h5>
                  <p  class="mb-0">{{ this.Model }}</p>
                </b-col>
              </b-row>
            </div>
          </div>
        </div>
      </div>
      <!-- ITEM -->
      <div class="row  mt-3">
        <div class="col-md-12">
          <div class="card">
            <div class="card-body p-0">
              <h5 class="card-title p-3 pb-0 mb-0">Item</h5>
              <b-row class="mr-3 p-3 pt-0">
                <b-col md="12" class="mt-3">
                  <b-form-select id="select-1" v-model="selItem" :options="optionsItems" @change="onItemChange($event)" required
                    value-field="id" text-field="txtDescription"> </b-form-select>
                </b-col>
              </b-row>
              <b-row class="mr-3 p-3 pt-0">
                <b-col md="3">
                  <h5>Article Number</h5>
                  <p  class="mb-0">{{ this.ItemArtNumber }}</p>
                </b-col>
                <b-col md="3">
                  <h5>Description</h5>
                  <p  class="mb-0">{{ this.ItemDescription }}</p>
                  </b-col>
                <b-col md="3">
                  <h5>Type</h5>
                  <p  class="mb-0">{{ this.ItemType }}</p>
                </b-col>
                <b-col md="3">
                  <h5>Version</h5>
                  <p  class="mb-0">{{ this.ItemVersion }}</p>
                </b-col>
              </b-row>
            </div>
          </div>
        </div>
      </div>

      <!-- INSPECTION PARAMETER -->
      <div class="row mt-3">
        <div class="col-md-12">
          <div class="card">
            <div class="card-body p-0">
              <h5 class="card-title p-3 pb-0 mb-0">Inspection Parameter</h5>
              <div class="mr-3 p-3 pt-0">
                <b-row class="ml-2 mr-2 mt-1 pb-4" v-if="this.att1.length > 1">
                  <b-col md="3" v-for="attribute in att1" :key="attribute.id">
                    <b-input-group class="mt-3">
                      <template v-slot:prepend>
                        <b-input-group-text style="font-weight: 800;">{{ attribute.txtNameAttribute }}</b-input-group-text>
                      </template>
                      <b-form-input v-model="attribute.txtValueDefault"></b-form-input>
                    </b-input-group>
                  </b-col>
                </b-row>
                <b-row class="ml-2 mr-2 mt-1 border-top pb-4" v-if="this.att2.length > 1">
                  <b-col md="3" v-for="attribute in att2" :key="attribute.id">
                    <b-input-group class="mt-3">
                      <template v-slot:prepend>
                        <b-input-group-text style="font-weight: 800;">{{ attribute.txtNameAttribute }}</b-input-group-text>
                      </template>
                      <b-form-input v-model="attribute.txtValueDefault"></b-form-input>
                    </b-input-group>
                  </b-col>
                </b-row>
                <b-row class="ml-2 mr-2 mt-1 border-top pb-4" v-if="this.att3.length > 1">
                  <b-col md="3" v-for="attribute in att3" :key="attribute.id">
                    <b-input-group class="mt-3">
                      <template v-slot:prepend>
                        <b-input-group-text style="font-weight: 800;">{{ attribute.txtNameAttribute }}</b-input-group-text>
                      </template>
                      <b-form-input v-model="attribute.txtValueDefault"></b-form-input>
                    </b-input-group>
                  </b-col>
                </b-row>
                <b-row class="ml-2 mr-2 mt-1 border-top pb-4" v-if="this.att4.length > 1">
                  <b-col md="3" v-for="attribute in att4" :key="attribute.id">
                    <b-input-group class="mt-3">
                      <template v-slot:prepend>
                        <b-input-group-text style="font-weight: 800;">{{ attribute.txtNameAttribute }}</b-input-group-text>
                      </template>
                      <b-form-select>
                        <b-form-select-option value="true">Yes</b-form-select-option>
                        <b-form-select-option value="false">No</b-form-select-option>
                      </b-form-select>
                    </b-input-group>
                  </b-col>
                </b-row>
                <b-row class="ml-2 mr-2 mt-1 border-top pb-4" v-if="this.att5.length > 1">
                  <b-col md="3" v-for="attribute in att5" :key="attribute.id">
                    <b-input-group class="mt-3">
                      <template v-slot:prepend>
                        <b-input-group-text style="font-weight: 800;">{{ attribute.txtNameAttribute }}</b-input-group-text>
                      </template>
                      <b-form-input v-model="attribute.txtValueDefault"></b-form-input>
                    </b-input-group>
                  </b-col>
                </b-row>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- COMMENT -->
      <div class="row mt-3">
        <div class="col-md-12">
          <div class="card">
            <div class="card-body p-0">
              <h5 class="card-title p-3 pb-0 mb-0">Release & Notes</h5>
              <b-row class="mr-2 ml-2 mt-4 p-3 pt-0">
                <b-col md="4">
                  <div>
                    <b-input-group>
                      <template v-slot:prepend>
                        <b-input-group-text readonly style="font-weight: 800;">Test Date</b-input-group-text>
                      </template>
                      <template v-slot:append>
                        <b-form-datepicker id="datepicker1" v-model="datInspection"></b-form-datepicker>
                      </template>
                    </b-input-group>
                  </div>
                </b-col>
                <b-col md="4">
                  <b-input-group>
                    <template v-slot:prepend>
                      <b-input-group-text readonly style="font-weight: 800;">Auditor</b-input-group-text>
                    </template>
                    <template v-slot:append variant="info">
                      <b-form-input v-model="Inspector" placeholder="Enter your initials ..."></b-form-input>
                    </template>
                  </b-input-group>
                </b-col>
                <b-col md="4">
                  <b-input-group>
                    <template v-slot:prepend>
                      <b-input-group-text readonly style="font-weight: 800;">Release</b-input-group-text>
                    </template>
                    <template v-slot:append variant="info">
                      <b-form-select id="select-2" v-model="IType" :options="optionsRelease" required ></b-form-select>
                    </template>
                  </b-input-group>
                </b-col>
              </b-row>
              <b-row  class="mr-2 ml-2 p-3 pt-0">
                <b-col md="4">
                  <b-input-group>
                    <template v-slot:prepend>
                      <b-input-group-text readonly style="font-weight: 800;">Requested By</b-input-group-text>
                    </template>
                    <template v-slot:append variant="info">
                      <b-form-input v-model="Inspector" placeholder="Enter your initials ..."></b-form-input>
                    </template>
                  </b-input-group>
                </b-col>
                <b-col md="4">
                  <div>
                    <b-input-group>
                      <template v-slot:prepend>
                        <b-input-group-text readonly style="font-weight: 800;">Requested On</b-input-group-text>
                      </template>
                      <template v-slot:append>
                        <b-form-datepicker id="datepicker2" v-model="datRequested"></b-form-datepicker>
                      </template>
                    </b-input-group>
                  </div>
                </b-col>
                <b-col md="4">
                  <div>
                    <b-input-group>
                      <template v-slot:prepend>
                        <b-input-group-text readonly style="font-weight: 800;">Delivered On</b-input-group-text>
                      </template>
                      <template v-slot:append>
                        <b-form-datepicker id="datepicker3" v-model="datDelivered"></b-form-datepicker>
                      </template>
                    </b-input-group>
                  </div>
                </b-col>
              </b-row>
              <b-row class="mr-2 ml-2 mb-3 p-3 pt-0">
                <b-col md="6" class="mt-3">
                  <p class="mb-1">Comment 1</p>
                  <b-form-textarea id="area-1" v-model="Comment1" placeholder="Enter something..." rows="3" max-rows="6"></b-form-textarea>
                </b-col>
                <b-col md="6" class="mt-3">
                  <p class="mb-1">Comment 2</p>
                  <b-form-textarea id="area-2" v-model="Comment2" placeholder="Enter something..." rows="3" max-rows="6"></b-form-textarea>
                </b-col>
              </b-row>
              <b-row class="mr-2 ml-2 mb-3 p-3 pt-0">
                <b-col md="4">
                  <b-form-group label="File Upload:" label-for="file-default">
                    <b-form-file v-model="file" id="file-default" multiple :file-name-formatter="formatNames"></b-form-file>
                  </b-form-group>
                </b-col>
              </b-row>
            </div>
          </div>
        </div>
      </div>
    <b-row class="ml-3 mr-3 mt-4">
      <b-button class="mr-3" variant="primary" to="inspection-list">Save Inspection</b-button>
      <b-button class="mr-3" variant="outline-primary">PDF</b-button>
    </b-row>
  </div>
  <!-- ============ Body content End ============= -->
</template>
<script>

import { apiService } from "@/common/api.service.js";
import { AgGridVue } from '@ag-grid-community/vue';
// import html2canvas from 'jspdf/dist/html2canvas.js';
// import jsPDF from "jspdf";
// import html2pdf from "vue-html2pdf/dist/html2pdf.bundle.min.js";
import $ from 'jquery';
import VueHtml2pdf from 'vue-html2pdf'

// Vue.use(VueHtml2pdf)

export default {
  metaInfo: {    
    title: "New Inspection"
  },
  components: {
    AgGridVue, VueHtml2pdf
  },
  data() {
    return {
      inspectionName: null,
      templates: [],
      attributes: [],
      items: [],
      testAtt: [],
      model: [],
      modelData: [],
      deviceModels: [],
      selDevice: null,
      selItem: null,
      text: null,
      error: false,
      InspectionNumber: null,
      INumber: '',
      IStatus: '',
      IType: '',
      datInspection: '',
      Inspector: '',
      Approval: '',
      Comment1: '',
      Comment2: '',
      ODevice: '',
      Manufacturer: '',
      Supplier: '',
      Model: '',
      ItemArtNumber: '',
      ItemType: '',
      ItemDescription: '',
      ItemVersion: '',
      file: [],
      optionsDeviceModel: [],
      optionsItems: [],
      optionsRelease: [
        { value: 'YES', text: 'Yes' },
        { value: 'NO', text: 'No' },
        { value: 'CONDITIONALLY', text: 'Conditionally' },
      ],
      att1: [],
      att2: [],
      att3: [],
      att4: [],
      att5: [],
    };
  },
  methods: {
    getInspectionNumber() {
      this.InspectionNumber = 'PN2020-001'
    },
    onDeviceChange(event) {
      let device = this.optionsDeviceModel.filter(el => el.id == event)
      this.Manufacturer = device[0].idModel.idManufacturer.txtManufacturerName
      this.Supplier = device[0].idModel.idSupplier.txtSupplierName
      this.Model = device[0].idModel.txtModelName
    },
    onItemChange(event) {
      let item = this.optionsItems.filter(el => el.id == event)
      this.ItemArtNumber = item[0].txtArticlenumber
      this.ItemDescription = item[0].txtDescription
      this.ItemType = item[0].txtType
      this.ItemVersion = item[0].txtVersion
    },
    createPDF() {
      // const pdf = new jsPDF()
      // const html = document.getElementById('pdfContent')
      // pdf.fromHTML(html,15,15,{width:150})
      // pdf.output('dataurlnewwindow')
    },
    getTemplates() {
      if (!this.error) {
        var tempId = localStorage.getItem('ITempID')
        let endpoint = `/api/inspection-template-list/${tempId}/`;
        apiService(endpoint)
          .then(data => {
            this.templates = data;
            var atts = this.templates.idInspectionTemplateAttribute
            for (var i = 0; i < atts.length; i++) {
              if (atts[i].txtMeasureUnit == 'mm')
                this.att1.push(atts[i])
              else if (atts[i].txtMeasureUnit == 'µm')
                this.att2.push(atts[i])
              else if (atts[i].txtMeasureUnit == 'g')
                this.att3.push(atts[i])
              else if (atts[i].txtValueType == 'BOOLEAN')
                this.att4.push(atts[i])
              else
                this.att5.push(atts[i])
            }
          })
        console.log(this.att2.length)
      }
    },
    getDevicModel() {
      if (!this.error) {
        let endpoint = `/api/device-list/`;
        apiService(endpoint)
          .then(data => {
            this.deviceModels.push(...data.results);
            this.optionsDeviceModel = this.deviceModels
          })
      }
    },
    getItems() {
      if (!this.error) {
        let endpoint = `/api/item-list/`;
        apiService(endpoint)
          .then(data => {
            this.items.push(...data.results);
            this.optionsItems = this.items
          })
      }
    },
    addTemplate() {
      if (this.INumber) {
        let endpoint = `/api/inspection/`;
        apiService(endpoint, "POST", { 
          txtInspectionNumber: this.INumber,
          txtInspectionStatus: this.IStatus,
          txtInspectionType: this.IType,
          datInspection: this.datInspection,
          txtInspector: this.Inspector,
          txtApproval: this.Approval,
          txtComment1: this.Comment1,
          txtComment2: this.Comment2,
          idOrderDevice: this.ODevice,
          })
          .then(data => {
            if (data){
              this.templates.unshift(data)
            } else {
              this.error = true;
            }
          })
        this.TempName = null;
        if (this.error) {
          this.error = false;
        }
        } else {
          this.error = true;
        }
    },
    emptyInput() {
      this.TempName = '',
      this.Type = [],
      this.optionsAttributes = [],
      this.$root.$emit('bv::toggle::collapse', 'collapse-o')
    },
  },
  created() {
    this.getTemplates();
    this.getItems();
    this.getDevicModel();
    this.getInspectionNumber();
  },
};
</script>
<style>
  i:focus,
  input:focus,
  select:focus,
  textarea:focus,
  button:focus {
      outline: none;
  }

  .input-group-append, .input-group-prepend, .dropdown-toggle {
    width: 50%!important;
  }
    .input-group-text {
    width: 100%!important;
  }

</style>
