import React from "react";
import { Button } from '@mui/material'
import { Link } from 'react-router-dom'
import Graph from "../../components/Graph";

const GraphPage = () => {
    return(
        <div>
            <Link to="/movie">
                <Button>Back</Button>
            </Link>
            <Graph />
        </div>
    )
}

export default GraphPage