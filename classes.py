from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from pathlib import Path



@dataclass
class Addon:
    name: str
    mod_version: str
    game_version: list
    path: Path
    is_dependency : bool
    cf_url: str = ''
    cf_id: int = 0

@dataclass
class Category:
    id: int
    gameId: int
    name: str
    slug: str
    url: str
    iconUrl: str
    dateModified: datetime
    isClass: Optional[bool]
    classId: Optional[int]
    parentCategoryId: Optional[int]
    displayIndex: Optional[int]

    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_url(self):
        return self.url





@dataclass
class ModLinks:
    websiteUrl: str
    wikiUrl: str
    issuesUrl: str
    sourceUrl: str


@dataclass
class ModAuthor:
    id: int
    name: str
    url: str


@dataclass
class ModAsset:
    id: int
    modId: int
    title: str
    description: str
    thumbnailUrl: str
    url: str


@dataclass
class Category:
    id: int
    gameId: int
    name: str
    slug: str
    url: str
    iconUrl: str
    dateModified: datetime
    isClass: Optional[bool]
    classId: Optional[int]
    parentCategoryId: Optional[int]
    displayIndex: Optional[int]


@dataclass
class FileHash:
    value: str
    algo: int


@dataclass
class SortableGameVersion:
    gameVersionName: str
    gameVersionPadded: str
    gameVersion: str
    gameVersionReleaseDate: datetime
    gameVersionTypeId: int


@dataclass
class FileDependency:
    modId: int
    relationType: int


@dataclass
class FileModule:
    name: str
    fingerprint: int


@dataclass
class File:
    id: int
    gameId: int
    modId: int
    isAvailable: bool
    displayName: str
    fileName: str
    releaseType: int
    fileStatus: int
    hashes: list[FileHash]
    fileDate: datetime
    fileLength: int
    downloadCount: int
    fileSizeOnDisk: int
    downloadUrl: Optional[str]
    gameVersions: list[str]
    sortableGameVersions: list[SortableGameVersion]
    dependencies: list[FileDependency]
    exposeAsAlternative: bool
    parentProjectFileId: Optional[int]
    alternateFileId: Optional[int]
    isServerPack: bool
    serverPackFileId: Optional[int]
    isEarlyAccessContent: bool
    earlyAccessEndDate: Optional[datetime]
    fileFingerprint: int
    modules: list[FileModule]


@dataclass
class FileIndex:
    gameVersion: str
    fileId: int
    filename: str
    releaseType: int
    gameVersionTypeId: int
    modLoader: Optional[int]


@dataclass
class Mod:
    id: int
    gameId: int
    name: str
    slug: str
    links: ModLinks
    summary: str
    status: int
    downloadCount: int
    isFeatured: bool
    primaryCategoryId: int
    categories: list[Category]
    classId: Optional[int]
    authors: list[ModAuthor]
    logo: Optional[ModAsset]
    screenshots: list[ModAsset]
    mainFileId: int
    latestFiles: list[File]
    latestFilesIndexes: list[FileIndex]
    latestEarlyAccessFilesIndexes: list[FileIndex]
    dateCreated: datetime
    dateModified: datetime
    dateReleased: datetime
    allowModDistribution: Optional[bool]
    gamePopularityRank: int
    isAvailable: bool
    thumbsUpCount: int
    rating: Optional[float]