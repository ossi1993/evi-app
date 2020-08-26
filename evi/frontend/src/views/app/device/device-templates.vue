<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <breadcumb :page="'Templates'" :folder="'Device'" />
    <b-row>
      <!-- ICON BG -->
      <b-col lg="6" md="6" sm="12">
        <b-card
          class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center"
        >
          <i class="i-File"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Templates</p>
            <p class="inline text-primary text-24 line-height-1 mb-2">{{ this.templates.length }}</p>
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
    title: "Templates"
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
      templates: [],
      show: false,
      visible: false,
      date: null,
      next: null,
      error: false,
    };
  },
  beforeMount() {
    this.gridOptions = {};
    this.columnDefs = [
      {headerName: "Model Name", field: "txtModelName", filter: 'agTextColumnFilter', checkboxSelection: true,},
      {headerName: "Manufacturer", field: "idManufacturer.txtManufacturerName", filter: 'agTextColumnFilter', editable: false},
      {headerName: "Supplier", field: "idSupplier.txtSupplierName", filter: 'agTextColumnFilter', editable: false},
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
      let endpoint = `/api/model/${event.node.data.id}/`;
      console.log(event.node.data.id)
      try {
        await apiService(endpoint, "PATCH", { 
          txtModelName: event.node.data.txtModelName,
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
    getTemplates() {
      if (!this.error) {
        let endpoint = `/api/device-template/`;
        apiService(endpoint)
          .then(data => {
            this.templates.push(...data.results);
          })
      }
    },
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
    openModal(params) {
      this.$bvModal
        .msgBoxConfirm("Are you sure you want to delete the selected Template?", {
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
            this.deleteModel();
          }
        })
    },
    async deleteModel() {
      var selectedRows = this.gridApi.getSelectedRows();
      let endpoint = `/api/device-template/${selectedRows[0].id}/`;
      try {
        var index = this.templates.map(function(e) { return e.id; }).indexOf(selectedRows[0].id);
        this.$delete(this.templates, index)
        await apiService(endpoint, "DELETE")
        this.show = this.show ? false : true
      }
      catch (err) {
        console.log(err)
      }
    },
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
    this.getTemplates();
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
