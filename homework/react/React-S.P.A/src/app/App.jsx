import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import { ActivitiesPage } from '../pages/ActivitiesPage/ActivitiesPage';
import { ActivityFormPage } from '../pages/ActivityFormPage/ActivityFormPage';

function App() {
    return(
        <BrowserRouter>
            <Routes>
                <Route path='/' element={<ActivitiesPage />}/>
                <Route path='/activities/new' element={<ActivityFormPage />}/>
                <Route path='/activities/edit/:id' element={<ActivityFormPage />}/>
                <Route path='*' element={<Navigate to="/" replace />}/>
            </Routes>
        </BrowserRouter>
    )
}

export default App;