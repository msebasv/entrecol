import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Sidebar from '../../components/Sidebar'
import TableMovie from '../../components/TableMovie'

import './index.css'

const columns = [
  { title: 'Id', headerName: 'Id', field: 'bookID', width: 60 },
  { title: 'Title', headerName: 'Title', field: 'title', width: 450 },
  { title: 'Author', headerName: 'Author', field: 'authors', width: 300 },
  { title: 'Pages', headerName: 'Pages', field: 'num_pages', width: 70 },
  {
    title: 'Language',
    headerName: 'Language',
    field: 'language_code',
    width: 70,
  },
  { title: 'Date', headerName: 'Date', field: 'publication_date', width: 100 },
  {
    title: 'Publisher',
    headerName: 'Publisher',
    field: 'publisher',
    width: 120,
  },
  { title: 'Rating', headerName: 'Rating', field: 'ratings_count', width: 110 },
]

const Movie = () => {
  const [data, setData] = useState([])
  const [pageSize, setPageSize] = useState(100)
  const [page, setPage] = useState(1)

  const getData = async () => {
    const url = `http://localhost:5000/books?_limit=${pageSize}&_page=${page}`
    const result = await axios.get(url)
    setData(result.data)
  }

  useEffect(() => {
    getData()
  }, [pageSize, page])

  const handleSelectedRows = (event) => {
    setPageSize(event.target.value)
  }

  return (
    <div className="container-movie">
      <Sidebar />
      <div className="content">
        <h2>Movies</h2>
        <TableMovie
          rows={data.map((movie) => movie)}
          columns={columns}
          size={pageSize}
          setSize={handleSelectedRows}
          page={page}
          setPage={setPage}
        />
      </div>
    </div>
  )
}

export default Movie
