<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <breadcumb :page="'List'" :folder="'Inspection'" />
    <b-row>
      <b-col lg="6" md="6" sm="12">
        <b-card class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center">
          <i class="i-File-Clipboard-File--Text"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Inspections</p>
            <p class="inline text-primary text-24 line-height-1 mb-2">{{ this.inspections.length }}</p>
          </div>
        </b-card>
      </b-col>
      <b-col lg="6" md="6" sm="12">
        <b-card class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center">
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
          <div class="card-body p-0">
            <AgGridVue class="ag-theme-alpine"
                id="gridInspection"
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
      <b-button class="mr-3" to="inspection" variant="primary">Edit Inspection</b-button>
      <b-button class="mr-3" variant="outline-primary">Delete Inspection</b-button>
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
    title: "Inspection"
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
      inspections: [],
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
      {headerName: "Inspection Number", field: "txtInspectionNumber", filter: 'agTextColumnFilter', checkboxSelection: true,},
      {headerName: "Inspection Status", field: "txtInspectionStatus", filter: 'agTextColumnFilter',},
      {headerName: "Inspection Type", field: "txtInspectionType", filter: 'agTextColumnFilter',},
      {headerName: "Inspection Date", field: "datInspection", filter: 'agTextColumnFilter',},
      {headerName: "Inspector", field: "txtInspector", filter: 'agTextColumnFilter',},
      {headerName: "Approval", field: "txtApproval", filter: 'agTextColumnFilter',},
      {headerName: "Comment 1", field: "txtComment1", filter: 'agTextColumnFilter',},
      {headerName: "Comment 2", field: "txtComment2", filter: 'agTextColumnFilter',},
    ],
    this.defaultColDef = {
      flex: 1,
      editable: false,
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
    async cellValueChanged(event) {     
      let endpoint = `/api/inspection/${event.node.data.id}/`;
      console.log(event.node.data.id)
      try {
        await apiService(endpoint, "PATCH", { 
          txtInspectionNumber: event.node.data.txtInspectionNumber,
          txtInspectionStatus: event.node.data.txtInspectionStatus,
          txtInspectionType: event.node.data.txtInspectionType,
          datInspection: event.node.data.datInspection,
          txtInspector: event.node.data.txtInspector,
          txtApproval: event.node.data.txtApproval,
          txtComment1: event.node.data.txtComment1,
          txtComment2: event.node.data.txtComment2,
          idOrderDevice: event.node.data.idOrderDevice,
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
    },
    getInspections() {
      if (!this.error) {
        let endpoint = `/api/inspection/`;
        apiService(endpoint)
          .then(data => {
            this.inspections.push(...data.results);
            this.rowData = this.inspections
          })
      }
    },
    openModal(params) {
      this.$bvModal
        .msgBoxConfirm("Are you sure you want to delete the selected Inspection?", {
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
            this.deleteInspection();
          }
        })
    },
    async deleteInspection() {
      var selectedRows = this.gridApi.getSelectedRows();
      let endpoint = `/api/inspection/${selectedRows[0].id}/`;
      try {
        var index = this.inspections.map(function(e) { return e.id; }).indexOf(selectedRows[0].id);
        this.$delete(this.inspections, index)
        await apiService(endpoint, "DELETE")
        this.show = this.show ? false : true
      }
      catch (err) {
        console.log(err)
      }
    },
    editInspection() {
      this.$route.push('inspection')
    },
    getDateToday() {
      var today = new Date();
      this.date = today.getDate()+' / '+(today.getMonth()+1)+' / '+today.getFullYear();
    },
  },
  created() {
    this.getInspections();
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
