import React, {useState} from 'react'

import { Button, Select, MenuItem } from '@mui/material'

import {
  DataGrid,
  gridPaginatedVisibleSortedGridRowIdsSelector,
  GridToolbar,
  GridToolbarContainer,
  useGridApiContext,
  GridLinkOperator
} from '@mui/x-data-grid'

import DatePicker from 'react-datepicker'

import "react-datepicker/dist/react-datepicker.css";

import './index.css'

const getRowsFromCurrentPage = ({ apiRef }) =>
  gridPaginatedVisibleSortedGridRowIdsSelector(apiRef)

const CustomToolbar = () => {
  const apiRef = useGridApiContext()

  const handleExport = (options) => {
    apiRef.current.exportDataAsPrint(options)
  }

  return (
    <GridToolbarContainer>
      <Button
        onClick={() =>
          handleExport({ getRowsToExport: getRowsFromCurrentPage })
        }
      >
        Export PDF
      </Button>
    </GridToolbarContainer>
  )
}

function CustomPagination(props) {
  const { page, setPage, size, setSize } = props

  return (
    <div>
      <Select
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        value={size}
        label="Rows"
        onChange={setSize}
      >
        <MenuItem value={5}>5</MenuItem>
        <MenuItem value={10}>10</MenuItem>
        <MenuItem value={15}>15</MenuItem>
        <MenuItem value={20}>20</MenuItem>
      </Select>
      <Button disabled={page <= 0} onClick={() => setPage(page - 1)}>
        Previous
      </Button>
      <Button onClick={() => setPage(page + 1)}>Next</Button>
    </div>
  )
}

const Date = () => {
  const [startDate, setStartDate] = useState(null);
  return (
    <DatePicker selected={startDate} onChange={date => setStartDate(date)} />
  );
}

const TableEmployee = (props) => {
  const { rows, columns, size, setSize, page, setPage } = props

  const Test = () => (
    <CustomPagination
      page={page}
      setPage={setPage}
      size={size}
      setSize={setSize}
    />
  )

  const Rows = () => {
    const emp = rows.map((employee)=>{
      return ({
        codigo: employee.codigo,
        nombre: employee.nombre,
        dependencia: employee.dependencia.nombre,
        cargo: employee.cargo.nombre,
        fecha_ingreso: employee.fecha_ingreso,
        eps: employee.eps.nombre,
        pension: employee.pension.nombre,
        rol: employee.rol.nombre,
        sueldo: employee.sueldo
      }
      )
    })
    return emp
  }

  return (
    <div className="container-table">
      <Date/>
      <DataGrid
        getRowId={(row) => row.codigo}
        rows={Rows()}
        columns={columns}
        rowsPerPageOptions={[5, 10 ,15]}
        components={{
          Toolbar: GridToolbar,
          Pagination: Test,
        }}
      pagination
      />
    </div>
  )
}

export default TableEmployee
