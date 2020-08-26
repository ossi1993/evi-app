<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <breadcumb :page="'Import'" :folder="'Item'" />

    <div class="row mt-5">
      <div class="col-md-12">
        <div class="card mb-30">
          <div class="card-body p-0">
            <AgGridVue class="ag-theme-alpine"
                id="gridImport"
                :defaultColDef="defaultColDef"
                :columnDefs="columnDefs"
                :rowSelection="rowSelection"
                :rowData="rowData"
                :gridOptions="gridOptions"
                :suppressRowClickSelection="true"
                @grid-ready="onGridReady"
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

    <b-row class="ml-1 mr-3 mb-6">
      <b-collapse v-model="show">
        <b-button class="mr-4" variant="primary">Save Item Selection</b-button>
        <b-button class="mr-4" @click="deleteInspection" variant="outline-primary">Delete Item Selection</b-button>
      </b-collapse>
    </b-row>

      <vue-csv-import class="ml-1 mr-3 mt-5"
        v-model="rowData" 
        :autoMatchFields="true"
        :headers="true"
        :canIgnore="true"
        :map-fields="['MANUFACTURER', 'MODEL', 'SUPPLIER', 'ARTICLE_NUMBER', 'TESTED_ON_ORIGINAL_DEVICE', 'GLUE_TYPE', 'PROTECTION_TYPE', 'OUTLINE', 'MEDIUM', 'EDGE_TREATMENT', 'WIDTH_IN_MM', 'LENGTH_IN_MM', 'THICKNESS_GLASS_IN_MYM', 'COST_IN_USD']">

        <template slot="hasHeaders" slot-scope="{headers, toggle}">
          <label>
            <input type="checkbox" id="hasHeaders" :value="headers" @change="toggle">
            Headers?
          </label>
        </template>

        <template slot="next" slot-scope="{load}">
          <b-button block variant="primary" @click.prevent="load">Load CSV</b-button>
          <!-- <button @click.prevent="load">load!</button> -->
        </template>    

        <template slot="submit" slot-scope="{submit}">
          <b-button variant="primary" @click.prevent="submit">Submit</b-button>
        </template>    
      </vue-csv-import>
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
import XLSX from 'xlsx';


export default {
  metaInfo: {    
    title: "Import"
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
      rowDataImport: null,
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
      templates: [],
      show: false,
      visible: false,
      date: null,
      next: null,
      error: false,
      file: null,
      excelFile: null,
      dataImport: '',
      csv: null,
      checked: true,
    };
  },
  beforeMount() {
    this.rowData = [];
    this.gridOptions = {};
    this.columnDefs = [
      {headerName: "Manufacturer", field: "MANUFACTURER", filter: 'agTextColumnFilter', checkboxSelection: true, headerCheckboxSelection: true,},
      {headerName: "Model", field: "MODEL", filter: 'agTextColumnFilter', },
      {headerName: "Supplier", field: "SUPPLIER", filter: 'agTextColumnFilter', },
      {headerName: "Article Number", field: "ARTICLE_NUMBER", filter: 'agTextColumnFilter', },
      {headerName: "Tested on Original Device", field: "TESTED_ON_ORIGINAL_DEVICE", filter: 'agTextColumnFilter', },
      {headerName: "Glue Type", field: "GLUE_TYPE", filter: 'agTextColumnFilter', },
      {headerName: "Protection Type", field: "PROTECTION_TYPE", filter: 'agTextColumnFilter', },
      {headerName: "Outline", field: "OUTLINE", filter: 'agTextColumnFilter', },
      {headerName: "Medium", field: "MEDIUM", filter: 'agTextColumnFilter', },
      {headerName: "Edge Treatment", field: "EDGE_TREATMENT", filter: 'agTextColumnFilter', },
      {headerName: "Width in mm", field: "WIDTH_IN_MM", filter: 'agTextColumnFilter', },
      {headerName: "Length in mm", field: "LENGTH_IN_MM", filter: 'agTextColumnFilter', },
      {headerName: "Thickness Glass in µm", field: "THICKNESS_GLASS_IN_MYM", filter: 'agTextColumnFilter', },
      {headerName: "Cost in USD", field: "COST_IN_USD", filter: 'agTextColumnFilter', },
    ],
    this.defaultColDef = {
      flex: 1,
      editable: true,
      resizable: true,
      sortable: true,
      filter: true,
      floatingFilter: true,
    };
    this.rowSelection = 'multiple';
    this.domLayout = 'autoHeight';
  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    this.gridColumnApi = this.gridOptions.columnApi;
    this.show = false;
  },
  methods: {
    onRowSelected(event) {
      this.show = true
      // this.show = this.show ? false : true
    },
    deleteInspection() {
      var index = this.gridApi.getSelectedNodes()[0].childIndex;
      this.$delete(this.rowData, index)
    },
    
    onGridReady(params) { 
    },

    onChangeInput(e) {
      this.importExcel(e);
    },

    addCssClass() {
      var element = document.getElementById("myDIV");
      element.classList.add("mystyle");    
    },

    // convertDataToWorkbook(data) {
    //   var data = new Uint8Array(data);
    //   var arr = new Array();
    //   for (var i = 0; i !== data.length; ++i) {
    //       arr[i] = String.fromCharCode(data[i]);
    //   }
    //   var bstr = arr.join("");
    //   return XLSX.read(bstr, {type: "binary"});
    // },


    // addTemplates() {
    //   if (this.MName) {
    //     let endpoint = `/api/device-template/`;
    //     apiService(endpoint, "POST", { 
    //       txtModelName: this.MName,
    //       idManufacturer: this.Manufacturer,
    //       idSupplier: this.Supplier,
    //       })
    //       .then(data => {
    //         if (data) {
    //           console.log(data)
    //           this.models.unshift(data)
    //         } else {
    //           this.error = true;
    //         }
    //       })
    //     this.emptyInput();
    //     if (this.error) {
    //       this.error = false;
    //     }
    //     } else {
    //       this.error = true;
    //     }
    // },
    // openModal(params) {
    //   this.$bvModal
    //     .msgBoxConfirm("Are you sure you want to delete the selected Template?", {
    //       title: "Please Confirm",
    //       size: "sm",
    //       buttonSize: "sm",
    //       okVariant: "danger",
    //       okTitle: "YES",
    //       cancelTitle: "NO",
    //       footerClass: "p-2",
    //       hideHeaderClose: false,
    //       centered: true
    //     })
    //     .then(value => {
    //       if (value) {
    //         this.deleteModel();
    //       }
    //     })
    // },
    // async deleteModel() {
    //   var selectedRows = this.gridApi.getSelectedRows();
    //   let endpoint = `/api/device-template/${selectedRows[0].id}/`;
    //   try {
    //     var index = this.templates.map(function(e) { return e.id; }).indexOf(selectedRows[0].id);
    //     this.$delete(this.templates, index)
    //     await apiService(endpoint, "DELETE")
    //     this.show = this.show ? false : true
    //   }
    //   catch (err) {
    //     console.log(err)
    //   }
    // },
    // emptyInput() {
    //   this.MName = '',
    //   this.Manufacturer = [],
    //   this.Supplier = [],

    //   this.$root.$emit('bv::toggle::collapse', 'collapse-e')
    // },
    getDateToday() {
      var today = new Date();
      this.date = today.getDate()+' / '+(today.getMonth()+1)+' / '+today.getFullYear();
    },
  },
  created() {
    // this.getTemplates();
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
