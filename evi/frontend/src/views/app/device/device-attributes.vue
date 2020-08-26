<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <breadcumb :page="'Device Attributes'" :folder="'Device'" />
    <b-row>
      <!-- ICON BG -->
      <b-col lg="6" md="6" sm="12">
        <b-card
          class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center"
        >
          <i class="i-Atom"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Attributes</p>
            <p class="inline text-primary text-24 line-height-1 mb-2">{{ this.attributes.length }}</p>
          </div>
        </b-card>
      </b-col>
      <b-col lg="6" md="6" sm="12">
        <b-card
          class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center"
        >
          <i class="i-Calendar"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Date</p>
            <p class="text-primary text-24 line-height-1 mb-2"><nobr>{{ this.date }}</nobr></p>
          </div>
        </b-card>
      </b-col>
    </b-row>
    <div class="row">
      <div class="col-md-12">
        <div class="card mb-30">
          <div class="card-body p-0 mb-3">
            <b-row class="ml-3">
              <i class="nav-icon i-Add mt-3" style="font-size: 20px" v-b-toggle.collapse-e></i>
              <h5 class="card-title border-bottom p-3 mb-2">New Device Attribute</h5>
            </b-row>
            <b-collapse id="collapse-e" class="mt-3">
              <b-form>
                <b-row class="ml-3 mr-3 mt-3">
                  <b-col md="4">
                    <b-form-input id="input-1" v-model="KeyAtt" type="text" required placeholder="Key Attribute" ></b-form-input>
                  </b-col>
                  <b-col md="4">
                    <b-form-input id="input-2" v-model="NameAtt" type="text" required placeholder="Name Attribute" ></b-form-input>
                  </b-col>
                  <b-col md="4">
                    <b-form-input id="input-3" v-model="ValueAtt" type="text" required placeholder="Value Attribute" ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3 mt-3">
                  <b-col md="4">
                    <b-form-select  id="select-1" v-model="ValueType" :options="optionsTypes" required ></b-form-select>
                  </b-col>
                  <b-col md="4">
                    <b-form-select  id="select-2" v-model="MeasureUnit" :options="optionsUnits" required ></b-form-select>
                  </b-col>
                  <b-col md="4">
                    <b-form-select  id="select-3" v-model="Device" :options="optionsDevices" required value-field="id" text-field="txtSerialNumber"></b-form-select>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3 mt-3">
                  <b-col md="6">
                    <b-button @click="emptyInput" block variant="outline-primary">Delete Input</b-button>
                  </b-col>
                  <b-col md="6">
                    <b-button @click="addAtt" block variant="primary">Add Attribute</b-button>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3">
                  <b-col md="12" class="mt-3">
                    <b-alert v-if="error" show variant="alert alert-card alert-danger" dismissible>
                      <strong class="text-capitalize">Error!</strong> The Input is not valid.
                    </b-alert>
                  </b-col>
                </b-row>
              </b-form>
            </b-collapse>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div class="card mb-30">
          <div class="card-body p-0">
            <AgGridVue class="ag-theme-alpine"
                id="gridAttributes"
                :defaultColDef="defaultColDef"
                :columnDefs="columnDefs"
                :rowSelection="rowSelection"
                :rowData="rowData"
                :gridOptions="gridOptions"
                :suppressRowClickSelection="true"
                @grid-ready="onGridReady"
                @cellValueChanged="cellValueChanged"
                @row-selected="onRowSelected"
                :masterDetail="true"
                :detailCellRendererParams="detailCellRendererParams"
                :pagination="true"
                :paginationPageSize="10"
                :domLayout="domLayout"
                :modules="modules">
            </AgGridVue>
          </div>
        </div>
      </div>
    </div>
    <b-collapse v-model="show" class="ml-1 mr-3">
      <b-button @click="openModal" variant="primary">Delete Attribute</b-button>
    </b-collapse>
  </div>
  <!-- ============ Body content End ============= -->
</template>
<script>
import { apiService } from "@/common/api.service.js";
import { AgGridVue } from '@ag-grid-community/vue';
import { ClientSideRowModelModule } from "@ag-grid-community/client-side-row-model";
import { RichSelectModule } from '@ag-grid-enterprise/rich-select';
import { MenuModule } from '@ag-grid-enterprise/menu';
import { ColumnsToolPanelModule } from '@ag-grid-enterprise/column-tool-panel';
import { SetFilterModule } from '@ag-grid-enterprise/set-filter';
import { AllCommunityModules } from '@ag-grid-community/all-modules';
import { MasterDetailModule } from '@ag-grid-enterprise/master-detail';

export default {
  metaInfo: {    
    title: "Device Attributes"
  },
  components: {
    AgGridVue
  },
  data() {
    return {
      gridOptions: null,
      gridApi: null,
      columnApi: null,
      columnDefs: null,
      columnDefsMod: null,
      rowData: null,
      rowDataMod: null,
      rowSelection: null,
      defaultColDef: null,
      frameworkComponents: null,
      detailCellRendererParams: null,
      domLayout: null,
      modules: [
        ClientSideRowModelModule,
        SetFilterModule,
        RichSelectModule,
        MenuModule,
        ColumnsToolPanelModule,
        MasterDetailModule,
      ],
      attributes: [],
      devices: [],
      show: false,
      visible: false,
      KeyAtt: '',
      NameAtt: '',
      ValueAtt: '',
      ValueType: '',
      MeasureUnit: '',
      Device: '',
      date: null,
      next: null,
      error: false,
      optionsDevices: [],
      optionsTypes: [
        { value: 'INTEGER', text: 'Number' },
        { value: 'FLOAT', text: 'Decimal' },
        { value: 'STRING', text: 'Text' },
        { value: 'BOOLEAN', text: 'True/False' },
      ],
      optionsUnits: [
        { value: 'mm', text: 'Millimetre' },
        { value: 'cm', text: 'Centimetre' },
        { value: 'mg', text: 'Milligram' },
        { value: 'g', text: 'Gram' },
        { value: 'ml', text: 'Millilitre' },
        { value: 'in', text: 'Inch' },
        { value: 'oz', text: 'Ounce' },
      ],
    };
  },
  beforeMount() {
    this.gridOptions = {};
    this.columnDefs = [
      {headerName: "Key Attribute", field: "txtKeyAttribute", filter: 'agTextColumnFilter', checkboxSelection: true,},
      {headerName: "Name Attribute", field: "txtNameAttribute", filter: 'agTextColumnFilter', },
      {headerName: "Value Attribute", field: "txtValueAttribute", filter: 'agTextColumnFilter', },
      {headerName: "Value Type", field: "txtValueType", filter: 'agTextColumnFilter', },
      {headerName: "Measure Unit", field: "txtMeasureUnit", filter: 'agTextColumnFilter', },
      {headerName: "Device", field: "idDevice", filter: 'agTextColumnFilter', editable: false},
    ],
    this.defaultColDef = {
      flex: 1,
      editable: true,
      resizable: true,
      sortable: true,
      filter: true,
      floatingFilter: true,
    };
    this.rowSelection = 'single';
    this.domLayout = 'autoHeight';
  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    this.gridColumnApi = this.gridOptions.columnApi;
  },
  methods: {
    autoSizeAll(skipHeader) {
      var allColumnIds = [];
      this.gridColumnApi.getAllColumns().forEach(function(column) {
        allColumnIds.push(column.colId);
      });
      this.gridColumnApi.autoSizeColumns(allColumnIds, skipHeader);
    },
    async cellValueChanged(event) {     
      let endpoint = `/api/device-attribute/${event.node.data.id}/`;
      try {
        await apiService(endpoint, "PATCH", { 
          txtKeyAttribute: event.node.data.txtKeyAttribute,
          txtNameAttribute: event.node.data.txtNameAttribute,
          txtValueAttribute: event.node.data.txtValueAttribute,
          txtValueType: event.node.data.txtValueType,
          txtMeasureUnit: event.node.data.txtMeasureUnit,
          idDevice: event.node.data.idDevice,
        })
      }
      catch (err) {
        console.log(err)
      }
    },
    onRowSelected(event) {
      this.show = this.show ? false : true
    },
    onGridReady(params) { 
      // this.autoSizeAll(false);
    },
    getAtt() {
      if (!this.error) {
        let endpoint = `/api/device-attribute/`;
        apiService(endpoint)
          .then(data => {
            this.attributes.push(...data.results);
            this.rowData = this.attributes
          })
      }
    },
    getDevices() {
      if (!this.error) {
        let endpoint = `/api/device/`;
        apiService(endpoint)
          .then(data => {
            this.devices.push(...data.results);
            this.optionsDevices = this.devices
          })
      }
    },
    addAtt() {
      if (this.KeyAtt) {
        let endpoint = `/api/device-attribute/`;
        apiService(endpoint, "POST", { 
          txtKeyAttribute: this.KeyAtt,
          txtNameAttribute: this.NameAtt,
          txtValueAttribute: this.ValueAtt,
          txtValueType: this.ValueType,
          txtMeasureUnit: this.MeasureUnit,
          idDevice: this.Device,
          })
          .then(data => {
            if (data){
              this.attributes.unshift(data)
            } else {
              this.error = true;
            }
          })
        this.emptyInput();
        if (this.error) {
          this.error = false;
        }
        } else {
          this.error = true;
        }
    },
    openModal(params) {
      this.$bvModal
        .msgBoxConfirm("Are you sure you want to delete the selected Attribute?", {
          title: "Please Confirm",
          size: "sm",
          buttonSize: "sm",
          okVariant: "danger",
          okTitle: "YES",
          cancelTitle: "NO",
          footerClass: "p-2",
          hideHeaderClose: false,
          centered: true
        })
        .then(value => {
          if (value) {
            this.deleteAttribute();
          }
        })
    },
    async deleteAttribute() {
      var selectedRows = this.gridApi.getSelectedRows();
      let endpoint = `/api/device-attribute/${selectedRows[0].id}/`;
      try {
        var index = this.attributes.map(function(e) { return e.id; }).indexOf(selectedRows[0].id);
        this.$delete(this.attributes, index)
        await apiService(endpoint, "DELETE")
        this.show = this.show ? false : true
      }
      catch (err) {
        console.log(err)
      }
    },
    emptyInput() {
      this.KeyAtt = '',
      this.NameAtt = '',
      this.ValueType = [],
      this.ValueAtt = '',
      this.MeasureUnit = '',
      this.Device = [],

      this.$root.$emit('bv::toggle::collapse', 'collapse-e')
    },
    getDateToday() {
      var today = new Date();
      this.date = today.getDate()+' / '+(today.getMonth()+1)+' / '+today.getFullYear();
    },
  },
  created() {
    this.getAtt();
    this.getDevices();
    this.getDateToday();
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
</style>
